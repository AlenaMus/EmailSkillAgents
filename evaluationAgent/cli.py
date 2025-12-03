"""
Command-line interface for Evaluation Gmail Sender Agent.

This module provides a Click-based CLI for creating and sending
evaluation emails to students.
"""

import click
from pathlib import Path
import sys

from .config import (
    VERSION,
    AGENT_NAME,
    DEFAULT_INPUT_FILE,
    DEFAULT_INSTRUCTOR_NAME,
)
from .email_sender import create_email_drafts
from .errors import (
    EvaluationAgentError,
    ExcelFileNotFoundError,
    ExcelReadError,
    ExcelValidationError,
    GmailAuthenticationError,
)


def print_banner():
    """Print application banner."""
    click.echo(f"\n{AGENT_NAME} v{VERSION}")
    click.echo("=" * 60)
    click.echo()


def print_success(message: str):
    """Print success message in green."""
    try:
        click.secho(f"✓ {message}", fg='green', bold=True)
    except UnicodeEncodeError:
        click.secho(f"[OK] {message}", fg='green', bold=True)


def print_error(message: str):
    """Print error message in red."""
    try:
        click.secho(f"✗ {message}", fg='red', bold=True)
    except UnicodeEncodeError:
        click.secho(f"[ERROR] {message}", fg='red', bold=True)


def print_warning(message: str):
    """Print warning message in yellow."""
    try:
        click.secho(f"⚠ {message}", fg='yellow')
    except UnicodeEncodeError:
        click.secho(f"[WARNING] {message}", fg='yellow')


@click.group()
@click.version_option(version=VERSION, prog_name=AGENT_NAME)
def cli():
    """
    Evaluation Gmail Sender Agent

    Automatically creates and sends personalized grade evaluation emails
    to students based on graded Excel files.
    """
    pass


@cli.command('create-drafts')
@click.option(
    '--input',
    'input_file',
    type=click.Path(exists=True, path_type=str),
    default=str(DEFAULT_INPUT_FILE),
    help='Path to Excel file with student grades',
)
@click.option(
    '--use-gmail',
    is_flag=True,
    default=False,
    help='Use Gmail API to create drafts (requires authentication)',
)
@click.option(
    '--to',
    'to_override',
    type=str,
    default=None,
    help='Override recipient email (for testing)',
)
@click.option(
    '--dry-run',
    is_flag=True,
    default=False,
    help='Preview only, do not create files or drafts',
)
@click.option(
    '--verbose',
    is_flag=True,
    default=False,
    help='Enable verbose output',
)
@click.option(
    '--instructor-name',
    type=str,
    default=DEFAULT_INSTRUCTOR_NAME,
    help='Instructor name for email signature',
)
def create_drafts_cmd(
    input_file: str,
    use_gmail: bool,
    to_override: str,
    dry_run: bool,
    verbose: bool,
    instructor_name: str,
):
    """
    Create email drafts for all students from Excel file.

    By default, emails are saved as HTML files in email_drafts/ folder.
    Use --use-gmail flag to create drafts in Gmail instead.

    Examples:

        # Create HTML files (default, safe)
        python -m evaluationAgent.cli create-drafts

        # Use custom input file
        python -m evaluationAgent.cli create-drafts --input myfile.xlsx

        # Send test email to yourself
        python -m evaluationAgent.cli create-drafts --to your@email.com

        # Create drafts in Gmail
        python -m evaluationAgent.cli create-drafts --use-gmail

        # Preview only (dry run)
        python -m evaluationAgent.cli create-drafts --dry-run

        # Verbose output
        python -m evaluationAgent.cli create-drafts --verbose
    """
    print_banner()

    # Validate input file
    if not Path(input_file).exists():
        print_error(f"Input file not found: {input_file}")
        click.echo()
        click.echo("Please provide a valid Excel file with student grades.")
        click.echo(f"Default expected location: {DEFAULT_INPUT_FILE}")
        sys.exit(1)

    # Show configuration
    mode = "Gmail API (drafts)" if use_gmail else "HTML files (local)"
    if dry_run:
        mode = "Dry-run (preview only)"

    click.echo(f"Mode:           {mode}")
    click.echo(f"Input File:     {input_file}")
    if to_override:
        click.echo(f"Test Recipient: {to_override}")
    click.echo(f"Instructor:     {instructor_name}")
    click.echo()

    # Confirmation for Gmail mode
    if use_gmail and not dry_run:
        print_warning("You are about to create drafts in Gmail.")
        if not click.confirm("Do you want to continue?"):
            click.echo("Cancelled.")
            sys.exit(0)

    # Execute
    try:
        click.echo("Processing students...")
        click.echo()

        result = create_email_drafts(
            input_file=input_file,
            use_gmail_api=use_gmail,
            to_override=to_override,
            dry_run=dry_run,
            verbose=verbose,
            instructor_name=instructor_name,
        )

        # Print summary
        click.echo()
        click.echo(result['summary'])

        # Success message
        stats = result['stats']
        if stats['created'] > 0:
            print_success(f"Created {stats['created']} email drafts successfully!")
        elif stats['skipped'] == stats['total']:
            print_warning("No valid students to process. All students were skipped.")
        else:
            print_warning("Completed with some students skipped or failed.")

        # Exit code
        if stats['failed'] > 0:
            sys.exit(1)
        else:
            sys.exit(0)

    except ExcelFileNotFoundError as e:
        print_error(f"Excel file not found: {e.filepath}")
        sys.exit(1)

    except ExcelReadError as e:
        print_error(f"Failed to read Excel file: {e.reason}")
        sys.exit(1)

    except ExcelValidationError as e:
        print_error(f"Invalid Excel file structure: {str(e)}")
        if e.missing_columns:
            click.echo(f"Missing columns: {', '.join(e.missing_columns)}")
        sys.exit(1)

    except GmailAuthenticationError as e:
        print_error(f"Gmail authentication failed: {str(e)}")
        click.echo()
        click.echo("To use Gmail API:")
        click.echo("1. Download credentials from Google Cloud Console")
        click.echo("2. Save as ~/.gmailagent/credentials.json")
        click.echo("3. Run authentication: python -m evaluationAgent.cli auth")
        sys.exit(1)

    except EvaluationAgentError as e:
        print_error(f"Error: {str(e)}")
        sys.exit(1)

    except KeyboardInterrupt:
        click.echo()
        print_warning("Cancelled by user")
        sys.exit(130)

    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@cli.command('auth')
@click.option(
    '--verbose',
    is_flag=True,
    default=False,
    help='Enable verbose output',
)
def auth_cmd(verbose: bool):
    """
    Authenticate with Gmail API.

    This will open a browser window to authorize the application
    to access your Gmail account. Required before using --use-gmail flag.
    """
    print_banner()

    click.echo("Gmail API Authentication")
    click.echo("-" * 60)
    click.echo()
    click.echo("This will authenticate with Gmail API and save credentials.")
    click.echo()

    if not click.confirm("Do you want to continue?"):
        click.echo("Cancelled.")
        sys.exit(0)

    try:
        from .gmail_client import GmailClient

        click.echo("Opening browser for authentication...")
        client = GmailClient(use_gmail_api=True, verbose=verbose)

        print_success("Authentication successful!")
        click.echo()
        click.echo("You can now use --use-gmail flag to create drafts in Gmail.")

    except GmailAuthenticationError as e:
        print_error(f"Authentication failed: {str(e)}")
        click.echo()
        click.echo("Make sure you have:")
        click.echo("1. Downloaded credentials.json from Google Cloud Console")
        click.echo("2. Saved it to ~/.gmailagent/credentials.json")
        sys.exit(1)

    except Exception as e:
        print_error(f"Error: {str(e)}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@cli.command('test')
@click.option(
    '--input',
    'input_file',
    type=click.Path(exists=True, path_type=str),
    default=str(DEFAULT_INPUT_FILE),
    help='Path to Excel file',
)
def test_cmd(input_file: str):
    """
    Test reading Excel file and validate data.

    This is a diagnostic command to verify the Excel file can be read
    and contains valid student data.
    """
    print_banner()

    click.echo("Testing Excel File")
    click.echo("-" * 60)
    click.echo(f"File: {input_file}")
    click.echo()

    try:
        from .excel_reader import read_students_from_excel, filter_valid_students

        # Read students
        click.echo("Reading Excel file...")
        students = read_students_from_excel(input_file)
        try:
            click.echo(f"✓ Found {len(students)} students")
        except UnicodeEncodeError:
            click.echo(f"[OK] Found {len(students)} students")
        click.echo()

        # Filter valid
        valid, invalid = filter_valid_students(students)
        click.echo(f"Valid for email:   {len(valid)}")
        click.echo(f"Skipped (invalid): {len(invalid)}")
        click.echo()

        # Show details
        if valid:
            click.echo("Valid students:")
            for i, student in enumerate(valid, 1):
                grade_display = f"{int(student.grade)}%" if student.grade == int(student.grade) else f"{student.grade:.1f}%"
                click.echo(f"  {i}. Grade: {grade_display} | Subject: {student.subject[:50]}")
            click.echo()

        if invalid:
            click.echo("Skipped students:")
            for i, student in enumerate(invalid, 1):
                reason = student.get_skip_reason()
                click.echo(f"  {i}. Reason: {reason} | Subject: {student.subject[:50]}")
            click.echo()

        print_success("Excel file is valid and ready to use!")

    except Exception as e:
        print_error(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    cli()
