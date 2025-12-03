"""
Email template generation for Evaluation Gmail Sender Agent.

This module handles the creation of professional HTML email templates
with personalized grading feedback.
"""

from typing import Optional
from .config import (
    COLOR_PRIMARY,
    COLOR_TEXT,
    COLOR_BACKGROUND_LIGHT,
    COLOR_LINK,
    DEFAULT_INSTRUCTOR_NAME,
)


def generate_email_html(
    grade: float,
    personalized_greeting: str,
    repo_url: str,
    student_name: str = "there",
    instructor_name: Optional[str] = None,
) -> str:
    """
    Generate HTML email content with personalized feedback.

    Args:
        grade: Student's grade (0-100)
        personalized_greeting: Personalized feedback message
        repo_url: Repository URL
        student_name: Student's name (default: "there")
        instructor_name: Instructor's name (default: from config)

    Returns:
        HTML email content as string

    Example:
        >>> html = generate_email_html(
        ...     grade=95,
        ...     personalized_greeting="Excellent work!",
        ...     repo_url="https://github.com/student/repo"
        ... )
    """
    if instructor_name is None:
        instructor_name = DEFAULT_INSTRUCTOR_NAME

    # Format grade display
    grade_display = f"{int(grade)}%" if grade == int(grade) else f"{grade:.1f}%"

    # Build HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment Feedback</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: {COLOR_TEXT};
            margin: 0;
            padding: 0;
            background-color: #ffffff;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 10px;
        }}
        .grade {{
            font-size: 24px;
            font-weight: bold;
            color: {COLOR_PRIMARY};
            margin: 20px 0;
            padding: 15px;
            background-color: {COLOR_BACKGROUND_LIGHT};
            border-radius: 5px;
            text-align: center;
        }}
        .feedback-box {{
            margin: 20px 0;
            padding: 15px;
            background-color: {COLOR_BACKGROUND_LIGHT};
            border-left: 4px solid {COLOR_PRIMARY};
            border-radius: 3px;
        }}
        .feedback-label {{
            font-weight: bold;
            font-size: 14px;
            color: {COLOR_PRIMARY};
            margin-bottom: 10px;
        }}
        .feedback-content {{
            font-size: 14px;
            line-height: 1.8;
            white-space: pre-wrap;
        }}
        .repo-section {{
            margin: 20px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 3px;
        }}
        .repo-label {{
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 8px;
        }}
        .repo-link {{
            color: {COLOR_LINK};
            text-decoration: none;
            font-size: 14px;
            word-break: break-all;
        }}
        .repo-link:hover {{
            text-decoration: underline;
        }}
        .signature {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            font-size: 14px;
        }}
        .signature-name {{
            font-weight: bold;
            margin-top: 5px;
        }}
        @media only screen and (max-width: 600px) {{
            .container {{
                padding: 10px;
            }}
            .grade {{
                font-size: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <p class="greeting">Hi {student_name},</p>

        <div class="grade">
            Your grade for this assignment: {grade_display}
        </div>

        <div class="feedback-box">
            <div class="feedback-label">Feedback:</div>
            <div class="feedback-content">{personalized_greeting}</div>
        </div>

        <div class="repo-section">
            <div class="repo-label">Repository:</div>
            <a href="{repo_url}" class="repo-link" target="_blank">{repo_url}</a>
        </div>

        <div class="signature">
            <p>Best regards,<br>
            <span class="signature-name">{instructor_name}</span></p>
        </div>
    </div>
</body>
</html>"""

    return html_template


def generate_plain_text(
    grade: float,
    personalized_greeting: str,
    repo_url: str,
    student_name: str = "there",
    instructor_name: Optional[str] = None,
) -> str:
    """
    Generate plain text email content (fallback for email clients that don't support HTML).

    Args:
        grade: Student's grade (0-100)
        personalized_greeting: Personalized feedback message
        repo_url: Repository URL
        student_name: Student's name (default: "there")
        instructor_name: Instructor's name (default: from config)

    Returns:
        Plain text email content as string
    """
    if instructor_name is None:
        instructor_name = DEFAULT_INSTRUCTOR_NAME

    # Format grade display
    grade_display = f"{int(grade)}%" if grade == int(grade) else f"{grade:.1f}%"

    plain_text = f"""Hi {student_name},

Your grade for this assignment: {grade_display}

Feedback:
{personalized_greeting}

Repository: {repo_url}

Best regards,
{instructor_name}
"""

    return plain_text


def validate_email_data(
    grade: float,
    personalized_greeting: str,
    repo_url: str,
) -> tuple[bool, Optional[str]]:
    """
    Validate email data before generation.

    Args:
        grade: Student's grade
        personalized_greeting: Personalized feedback
        repo_url: Repository URL

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check grade range
    if not isinstance(grade, (int, float)):
        return False, f"Grade must be a number, got {type(grade)}"

    if grade < 0 or grade > 100:
        return False, f"Grade must be between 0-100, got {grade}"

    # Check greeting
    if not personalized_greeting or not isinstance(personalized_greeting, str):
        return False, "Personalized greeting is required"

    if len(personalized_greeting.strip()) == 0:
        return False, "Personalized greeting cannot be empty"

    # Check repo URL
    if not repo_url or not isinstance(repo_url, str):
        return False, "Repository URL is required"

    if not repo_url.startswith(('http://', 'https://')):
        return False, f"Repository URL must start with http:// or https://, got: {repo_url}"

    return True, None


def extract_student_name(subject: str) -> str:
    """
    Extract student name from email subject (if possible).

    Args:
        subject: Email subject line

    Returns:
        Student name or "there" if not found
    """
    # For now, return generic greeting
    # Could be enhanced to parse names from subject line
    return "there"
