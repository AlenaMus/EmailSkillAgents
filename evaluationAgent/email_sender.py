"""
Main email sender orchestrator for Evaluation Gmail Sender Agent.

This module coordinates the entire email sending workflow:
reading Excel, generating emails, and saving/sending them.
"""

from pathlib import Path
from typing import Optional, List, Tuple
from datetime import datetime

from .config import (
    EMAIL_DRAFTS_DIR,
    DEFAULT_RECIPIENT,
    EMAIL_ENCODING,
    get_email_draft_filename,
    get_summary_filepath,
    ensure_directories,
)
from .excel_reader import (
    read_students_from_excel,
    filter_valid_students,
    StudentData,
)
from .email_template import (
    generate_email_html,
    generate_plain_text,
    validate_email_data,
    extract_student_name,
)
from .gmail_client import GmailClient
from .errors import FileSystemError


class EmailSender:
    """Main orchestrator for sending evaluation emails."""

    def __init__(
        self,
        use_gmail_api: bool = False,
        to_override: Optional[str] = None,
        dry_run: bool = False,
        verbose: bool = False,
        instructor_name: Optional[str] = None,
    ):
        """
        Initialize email sender.

        Args:
            use_gmail_api: If True, use Gmail API. If False, save to files (default).
            to_override: Override recipient email (for testing)
            dry_run: If True, don't save/send anything, just show what would happen
            verbose: Enable verbose logging
            instructor_name: Instructor's name for email signature
        """
        self.use_gmail_api = use_gmail_api
        self.to_override = to_override
        self.dry_run = dry_run
        self.verbose = verbose
        self.instructor_name = instructor_name

        # Initialize Gmail client if needed
        self.gmail_client = None
        if use_gmail_api and not dry_run:
            self.gmail_client = GmailClient(use_gmail_api=True, verbose=verbose)

        # Statistics
        self.stats = {
            'total': 0,
            'valid': 0,
            'skipped': 0,
            'created': 0,
            'failed': 0,
            'skip_reasons': [],
            'failed_reasons': [],
        }

    def create_drafts(self, input_file: str) -> dict:
        """
        Create email drafts for all students from Excel file.

        Args:
            input_file: Path to Excel file with student data

        Returns:
            Dictionary with statistics and results

        Raises:
            ExcelFileNotFoundError: If input file doesn't exist
            ExcelReadError: If file cannot be read
        """
        # Ensure directories exist
        ensure_directories()

        # Read students from Excel
        if self.verbose:
            print(f"Reading input file: {input_file}")

        students = read_students_from_excel(input_file)
        self.stats['total'] = len(students)

        if self.verbose:
            print(f"Found {len(students)} students")

        # Filter valid students
        valid_students, invalid_students = filter_valid_students(students)
        self.stats['valid'] = len(valid_students)
        self.stats['skipped'] = len(invalid_students)

        # Log skipped students
        for student in invalid_students:
            reason = student.get_skip_reason()
            self.stats['skip_reasons'].append({
                'id': student.id[:8],
                'subject': student.subject[:50],
                'reason': reason,
            })
            if self.verbose:
                print(f"Skipping student {student.id[:8]}: {reason}")

        # Process valid students
        created_files = []
        for idx, student in enumerate(valid_students, 1):
            try:
                result = self._process_student(idx, student)
                if result:
                    created_files.append(result)
                    self.stats['created'] += 1
            except Exception as e:
                self.stats['failed'] += 1
                self.stats['failed_reasons'].append({
                    'id': student.id[:8],
                    'subject': student.subject[:50],
                    'error': str(e),
                })
                if self.verbose:
                    print(f"Failed to process student {student.id[:8]}: {str(e)}")

        # Generate summary
        summary = self._generate_summary(created_files)

        # Save summary to file (if not dry-run)
        if not self.dry_run:
            self._save_summary(summary)

        return {
            'stats': self.stats,
            'summary': summary,
            'created_files': created_files,
        }

    def _process_student(self, index: int, student: StudentData) -> Optional[str]:
        """
        Process a single student: generate and save/send email.

        Args:
            index: Student index (1-based)
            student: Student data

        Returns:
            Path to created file (if file mode) or draft ID (if Gmail mode)
        """
        # Determine recipient
        recipient = self.to_override or DEFAULT_RECIPIENT

        # Extract student name
        student_name = extract_student_name(student.subject)

        # Validate email data
        is_valid, error_msg = validate_email_data(
            student.grade,
            student.personalized_greeting,
            student.url,
        )
        if not is_valid:
            raise ValueError(f"Invalid email data: {error_msg}")

        # Generate email content
        html_body = generate_email_html(
            grade=student.grade,
            personalized_greeting=student.personalized_greeting,
            repo_url=student.url,
            student_name=student_name,
            instructor_name=self.instructor_name,
        )

        plain_body = generate_plain_text(
            grade=student.grade,
            personalized_greeting=student.personalized_greeting,
            repo_url=student.url,
            student_name=student_name,
            instructor_name=self.instructor_name,
        )

        # Display progress
        total = self.stats['valid']
        grade_display = f"{int(student.grade)}%" if student.grade == int(student.grade) else f"{student.grade:.1f}%"
        print(f"[{index}/{total}] Student (Grade: {grade_display}) ", end='')

        # Dry run mode - just show what would happen
        if self.dry_run:
            print(f"-> Would create draft for {recipient} (DRY RUN)")
            return None

        # Gmail API mode
        if self.use_gmail_api and self.gmail_client:
            try:
                draft_id = self.gmail_client.create_draft(
                    to=recipient,
                    subject=student.subject,
                    html_body=html_body,
                    plain_body=plain_body,
                )
                print(f"-> Created Gmail draft (ID: {draft_id})")
                return draft_id
            except Exception as e:
                print(f"-> Failed: {str(e)}")
                raise

        # File mode (default) - save to HTML file
        else:
            filename = get_email_draft_filename(index, student.grade, recipient)
            filepath = EMAIL_DRAFTS_DIR / filename

            try:
                with open(filepath, 'w', encoding=EMAIL_ENCODING) as f:
                    f.write(html_body)

                print(f"-> Saved to {filename}")
                return str(filepath)
            except Exception as e:
                print(f"-> Failed to save: {str(e)}")
                raise FileSystemError("save_email", str(filepath), str(e))

    def _generate_summary(self, created_files: List[str]) -> str:
        """
        Generate summary report.

        Args:
            created_files: List of created file paths or draft IDs

        Returns:
            Summary text
        """
        mode = "Gmail API" if self.use_gmail_api else "Dry-Run (HTML files)"
        if self.dry_run:
            mode = "Dry-Run (preview only)"

        lines = [
            "=" * 60,
            "EVALUATION GMAIL SENDER - SUMMARY",
            "=" * 60,
            "",
            f"Mode: {mode}",
            f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "STATISTICS",
            "-" * 60,
            f"Total Students:        {self.stats['total']}",
            f"Valid for Email:       {self.stats['valid']}",
            f"Emails Created:        {self.stats['created']}",
            f"Skipped:               {self.stats['skipped']}",
            f"Failed:                {self.stats['failed']}",
            "",
        ]

        # Skipped students
        if self.stats['skip_reasons']:
            lines.append("SKIPPED STUDENTS")
            lines.append("-" * 60)
            for skip in self.stats['skip_reasons']:
                lines.append(f"  - ID: {skip['id']}... | Reason: {skip['reason']}")
                if self.verbose:
                    lines.append(f"    Subject: {skip['subject']}")
            lines.append("")

        # Failed students
        if self.stats['failed_reasons']:
            lines.append("FAILED STUDENTS")
            lines.append("-" * 60)
            for fail in self.stats['failed_reasons']:
                lines.append(f"  - ID: {fail['id']}... | Error: {fail['error']}")
                if self.verbose:
                    lines.append(f"    Subject: {fail['subject']}")
            lines.append("")

        # Created files/drafts
        if created_files and not self.dry_run:
            lines.append("CREATED EMAILS")
            lines.append("-" * 60)
            if self.use_gmail_api:
                lines.append(f"  {len(created_files)} drafts created in Gmail")
                if self.verbose:
                    for draft_id in created_files:
                        lines.append(f"    - Draft ID: {draft_id}")
            else:
                lines.append(f"  Output Directory: {EMAIL_DRAFTS_DIR}")
                lines.append(f"  Files Created:")
                for filepath in created_files:
                    filename = Path(filepath).name
                    lines.append(f"    - {filename}")
            lines.append("")

        # Next steps
        lines.append("NEXT STEPS")
        lines.append("-" * 60)
        if self.dry_run:
            lines.append("  1. Remove --dry-run flag to create actual drafts")
            lines.append("  2. Review settings and run again")
        elif not self.use_gmail_api:
            lines.append(f"  1. Review email content in {EMAIL_DRAFTS_DIR}/")
            lines.append("  2. To send via Gmail, use --use-gmail flag")
            lines.append("  3. Set up Gmail API credentials if needed")
        else:
            lines.append("  1. Review drafts in Gmail")
            lines.append("  2. Send drafts to students")
            lines.append("  3. Monitor student responses")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    def _save_summary(self, summary: str) -> None:
        """
        Save summary to file.

        Args:
            summary: Summary text to save
        """
        summary_path = get_summary_filepath()

        try:
            with open(summary_path, 'w', encoding=EMAIL_ENCODING) as f:
                f.write(summary)

            if self.verbose:
                print(f"\nSummary saved to: {summary_path}")

        except Exception as e:
            print(f"Warning: Failed to save summary: {str(e)}")


def create_email_drafts(
    input_file: str,
    use_gmail_api: bool = False,
    to_override: Optional[str] = None,
    dry_run: bool = False,
    verbose: bool = False,
    instructor_name: Optional[str] = None,
) -> dict:
    """
    Convenience function to create email drafts.

    Args:
        input_file: Path to Excel file
        use_gmail_api: Use Gmail API (default: False)
        to_override: Override recipient email
        dry_run: Preview only mode
        verbose: Enable verbose logging
        instructor_name: Instructor's name for signature

    Returns:
        Dictionary with statistics and results
    """
    sender = EmailSender(
        use_gmail_api=use_gmail_api,
        to_override=to_override,
        dry_run=dry_run,
        verbose=verbose,
        instructor_name=instructor_name,
    )

    return sender.create_drafts(input_file)
