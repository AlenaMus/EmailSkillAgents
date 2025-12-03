"""
Configuration constants for Evaluation Gmail Sender Agent.

This module contains all configuration settings, defaults, and constants
used throughout the agent.
"""

import os
from pathlib import Path
from typing import Final

# Version
VERSION: Final[str] = "1.0.0"
AGENT_NAME: Final[str] = "Evaluation Gmail Sender"

# Paths
PROJECT_ROOT: Final[Path] = Path(__file__).parent.parent
EMAIL_DRAFTS_DIR: Final[Path] = PROJECT_ROOT / "email_drafts"
GREETINGS_RESULTS_DIR: Final[Path] = PROJECT_ROOT / "greetings_results"
DEFAULT_INPUT_FILE: Final[Path] = GREETINGS_RESULTS_DIR / "homework_emails_with_greetings.xlsx"

# Gmail API Settings
GMAIL_SCOPES: Final[list] = [
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.labels',
]
GMAIL_LABEL_NAME: Final[str] = "lesson19Agents"
GMAIL_TOKEN_DIR: Final[Path] = Path.home() / ".gmailagent"
GMAIL_TOKEN_FILE: Final[Path] = GMAIL_TOKEN_DIR / "token.json"
GMAIL_CREDENTIALS_FILE: Final[Path] = GMAIL_TOKEN_DIR / "credentials.json"

# Excel Column Names
EXCEL_COLUMNS: Final[dict] = {
    'id': 'ID',
    'date': 'Date',
    'subject': 'Subject',
    'url': 'URL',
    'grade': 'Grade',
    'total_files': 'Total Files',
    'files_under_130': 'Files <130',
    'total_lines': 'Total Lines',
    'status': 'Status',
    'error_message': 'Error Message',
    'personalized_greeting': 'Personalized Greeting',
    'greeting_persona': 'Greeting Persona',
}

# Email Template Settings
DEFAULT_RECIPIENT: Final[str] = "test@example.com"
DEFAULT_INSTRUCTOR_NAME: Final[str] = "Your Instructor"
EMAIL_ENCODING: Final[str] = "utf-8"

# Processing Settings
SKIP_INVALID_GRADES: Final[bool] = True
SKIP_FAILED_REPOS: Final[bool] = True
MIN_VALID_GRADE: Final[float] = 0.0

# Retry Settings (for Gmail API)
MAX_RETRIES: Final[int] = 3
RETRY_DELAY: Final[float] = 1.0  # seconds
RETRY_BACKOFF: Final[float] = 2.0  # exponential backoff multiplier

# Output Settings
VERBOSE_OUTPUT: Final[bool] = False
SHOW_PROGRESS: Final[bool] = True

# Email Template Colors
COLOR_PRIMARY: Final[str] = "#2c5aa0"
COLOR_TEXT: Final[str] = "#333333"
COLOR_BACKGROUND_LIGHT: Final[str] = "#f5f5f5"
COLOR_LINK: Final[str] = "#0066cc"

# Summary Settings
SUMMARY_FILENAME: Final[str] = "summary.txt"


def ensure_directories() -> None:
    """Ensure all required directories exist."""
    EMAIL_DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    GREETINGS_RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def get_email_draft_filename(index: int, grade: float, recipient: str) -> str:
    """
    Generate email draft filename.

    Args:
        index: Email index (1-based)
        grade: Student grade
        recipient: Email recipient

    Returns:
        Filename for the email draft
    """
    # Sanitize recipient for filename
    safe_recipient = recipient.replace('@', '_at_').replace('.', '_')
    return f"email_{index}_grade_{int(grade)}_{safe_recipient}.html"


def get_summary_filepath() -> Path:
    """Get the path for the summary file."""
    return EMAIL_DRAFTS_DIR / SUMMARY_FILENAME
