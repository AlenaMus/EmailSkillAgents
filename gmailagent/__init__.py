"""
GmailAgent - Gmail Email Exporter

A Gmail automation tool that retrieves emails from Gmail using the Gmail API
based on specific filters and exports them to structured Excel documents with
URL extraction.
"""

__version__ = "1.0.0"
__author__ = "Product Team"
__license__ = "MIT"

from .auth import GmailAuthenticator
from .gmail_client import GmailClient
from .url_extractor import URLExtractor, extract_urls_from_emails
from .excel_exporter import ExcelExporter, export_emails_to_excel

__all__ = [
    'GmailAuthenticator',
    'GmailClient',
    'URLExtractor',
    'extract_urls_from_emails',
    'ExcelExporter',
    'export_emails_to_excel',
]
