"""
Evaluation Gmail Sender Agent

Automatically creates and sends personalized grade evaluation emails
to students based on graded Excel files.

This is the fourth and final agent in the automated homework grading workflow:
1. GmailAgent: Exports emails to Excel
2. Repository Analyzer: Analyzes repos and calculates grades
3. Personalized Greetings: Adds persona-based feedback
4. Evaluation Gmail Sender: Sends feedback to students (THIS AGENT)

Features:
- Read Excel files with grades and personalized greetings
- Generate professional HTML email templates
- Save emails as HTML files (default, safe mode)
- Create drafts in Gmail (optional, requires API setup)
- Test mode (send all to one recipient)
- Dry-run mode (preview without creating)

Usage:
    # Create HTML email files (default, safe)
    python -m evaluationAgent.cli create-drafts

    # Create drafts in Gmail
    python -m evaluationAgent.cli create-drafts --use-gmail

    # Test mode (send to yourself)
    python -m evaluationAgent.cli create-drafts --to your@email.com

    # Dry run (preview only)
    python -m evaluationAgent.cli create-drafts --dry-run

Version: 1.0.0
"""

from .config import VERSION, AGENT_NAME
from .email_sender import EmailSender, create_email_drafts
from .excel_reader import ExcelReader, StudentData, read_students_from_excel
from .email_template import generate_email_html, generate_plain_text
from .gmail_client import GmailClient
from .errors import (
    EvaluationAgentError,
    ExcelError,
    ExcelFileNotFoundError,
    ExcelReadError,
    ExcelValidationError,
    GmailError,
    GmailAuthenticationError,
    GmailAPIError,
    EmailGenerationError,
)

__version__ = VERSION
__all__ = [
    # Core
    'EmailSender',
    'create_email_drafts',
    # Excel
    'ExcelReader',
    'StudentData',
    'read_students_from_excel',
    # Email
    'generate_email_html',
    'generate_plain_text',
    # Gmail
    'GmailClient',
    # Errors
    'EvaluationAgentError',
    'ExcelError',
    'ExcelFileNotFoundError',
    'ExcelReadError',
    'ExcelValidationError',
    'GmailError',
    'GmailAuthenticationError',
    'GmailAPIError',
    'EmailGenerationError',
    # Metadata
    'VERSION',
    'AGENT_NAME',
]
