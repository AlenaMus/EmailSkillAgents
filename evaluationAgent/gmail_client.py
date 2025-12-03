"""
Gmail API client wrapper for Evaluation Gmail Sender Agent.

This module provides a wrapper around the Gmail API for creating drafts
and sending emails. Supports both real Gmail API mode and mock/dry-run mode.
"""

import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Optional, List
import time

from .config import (
    GMAIL_SCOPES,
    GMAIL_LABEL_NAME,
    GMAIL_TOKEN_FILE,
    GMAIL_CREDENTIALS_FILE,
    MAX_RETRIES,
    RETRY_DELAY,
    RETRY_BACKOFF,
)
from .errors import (
    GmailAuthenticationError,
    GmailAPIError,
    GmailLabelError,
)


class GmailClient:
    """Gmail API client wrapper with support for mock/dry-run mode."""

    def __init__(self, use_gmail_api: bool = False, verbose: bool = False):
        """
        Initialize Gmail client.

        Args:
            use_gmail_api: If True, use real Gmail API. If False, use mock mode.
            verbose: Enable verbose logging
        """
        self.use_gmail_api = use_gmail_api
        self.verbose = verbose
        self.service = None
        self.label_id = None

        if use_gmail_api:
            self._authenticate()
            self._ensure_label_exists()

    def _authenticate(self) -> None:
        """
        Authenticate with Gmail API using stored credentials.

        Raises:
            GmailAuthenticationError: If authentication fails
        """
        try:
            from google.auth.transport.requests import Request
            from google.oauth2.credentials import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            from googleapiclient.discovery import build

            creds = None

            # Load token if exists
            if GMAIL_TOKEN_FILE.exists():
                creds = Credentials.from_authorized_user_file(str(GMAIL_TOKEN_FILE), GMAIL_SCOPES)

            # If no valid credentials, authenticate
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    if not GMAIL_CREDENTIALS_FILE.exists():
                        raise GmailAuthenticationError(
                            f"Credentials file not found: {GMAIL_CREDENTIALS_FILE}. "
                            "Please download credentials from Google Cloud Console."
                        )
                    flow = InstalledAppFlow.from_client_secrets_file(
                        str(GMAIL_CREDENTIALS_FILE), GMAIL_SCOPES
                    )
                    creds = flow.run_local_server(port=0)

                # Save token
                GMAIL_TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
                with open(GMAIL_TOKEN_FILE, 'w') as token:
                    token.write(creds.to_json())

            # Build service
            self.service = build('gmail', 'v1', credentials=creds)

            if self.verbose:
                print("Gmail API authentication successful")

        except Exception as e:
            raise GmailAuthenticationError(f"Authentication failed: {str(e)}")

    def _ensure_label_exists(self) -> None:
        """
        Ensure the required Gmail label exists, create if not.

        Raises:
            GmailLabelError: If label operations fail
        """
        if not self.use_gmail_api:
            return

        try:
            # List all labels
            results = self.service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])

            # Find our label
            for label in labels:
                if label['name'] == GMAIL_LABEL_NAME:
                    self.label_id = label['id']
                    if self.verbose:
                        print(f"Found label '{GMAIL_LABEL_NAME}' with ID: {self.label_id}")
                    return

            # Label doesn't exist, create it
            label_object = {
                'name': GMAIL_LABEL_NAME,
                'labelListVisibility': 'labelShow',
                'messageListVisibility': 'show'
            }
            created_label = self.service.users().labels().create(
                userId='me',
                body=label_object
            ).execute()

            self.label_id = created_label['id']
            if self.verbose:
                print(f"Created label '{GMAIL_LABEL_NAME}' with ID: {self.label_id}")

        except Exception as e:
            raise GmailLabelError(GMAIL_LABEL_NAME, str(e))

    def create_draft(
        self,
        to: str,
        subject: str,
        html_body: str,
        plain_body: Optional[str] = None,
    ) -> Optional[str]:
        """
        Create a Gmail draft.

        Args:
            to: Recipient email address
            subject: Email subject
            html_body: HTML email body
            plain_body: Plain text email body (optional)

        Returns:
            Draft ID if using Gmail API, None in mock mode

        Raises:
            GmailAPIError: If draft creation fails
        """
        if not self.use_gmail_api:
            # Mock mode - just log
            if self.verbose:
                print(f"[MOCK] Would create draft to: {to}")
            return None

        # Build message
        message = self._create_message(to, subject, html_body, plain_body)

        # Create draft with retry logic
        for attempt in range(MAX_RETRIES):
            try:
                draft = self.service.users().drafts().create(
                    userId='me',
                    body={'message': message}
                ).execute()

                draft_id = draft['id']

                # Apply label if available
                if self.label_id:
                    self._apply_label_to_message(draft['message']['id'])

                if self.verbose:
                    print(f"Created draft ID: {draft_id}")

                return draft_id

            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    delay = RETRY_DELAY * (RETRY_BACKOFF ** attempt)
                    if self.verbose:
                        print(f"Retry {attempt + 1}/{MAX_RETRIES} after {delay}s: {str(e)}")
                    time.sleep(delay)
                else:
                    raise GmailAPIError("create_draft", str(e))

    def send_email(
        self,
        to: str,
        subject: str,
        html_body: str,
        plain_body: Optional[str] = None,
    ) -> Optional[str]:
        """
        Send an email directly (not as draft).

        Args:
            to: Recipient email address
            subject: Email subject
            html_body: HTML email body
            plain_body: Plain text email body (optional)

        Returns:
            Message ID if using Gmail API, None in mock mode

        Raises:
            GmailAPIError: If sending fails
        """
        if not self.use_gmail_api:
            # Mock mode - just log
            if self.verbose:
                print(f"[MOCK] Would send email to: {to}")
            return None

        # Build message
        message = self._create_message(to, subject, html_body, plain_body)

        # Send with retry logic
        for attempt in range(MAX_RETRIES):
            try:
                sent_message = self.service.users().messages().send(
                    userId='me',
                    body=message
                ).execute()

                message_id = sent_message['id']

                # Apply label if available
                if self.label_id:
                    self._apply_label_to_message(message_id)

                if self.verbose:
                    print(f"Sent email ID: {message_id}")

                return message_id

            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    delay = RETRY_DELAY * (RETRY_BACKOFF ** attempt)
                    if self.verbose:
                        print(f"Retry {attempt + 1}/{MAX_RETRIES} after {delay}s: {str(e)}")
                    time.sleep(delay)
                else:
                    raise GmailAPIError("send_email", str(e))

    def _create_message(
        self,
        to: str,
        subject: str,
        html_body: str,
        plain_body: Optional[str] = None,
    ) -> dict:
        """
        Create email message in Gmail API format.

        Args:
            to: Recipient email
            subject: Email subject
            html_body: HTML body
            plain_body: Plain text body (optional)

        Returns:
            Message dictionary for Gmail API
        """
        # Create multipart message
        message = MIMEMultipart('alternative')
        message['to'] = to
        message['subject'] = subject

        # Add plain text part if provided
        if plain_body:
            part1 = MIMEText(plain_body, 'plain', 'utf-8')
            message.attach(part1)

        # Add HTML part
        part2 = MIMEText(html_body, 'html', 'utf-8')
        message.attach(part2)

        # Encode message
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

        return {'raw': raw}

    def _apply_label_to_message(self, message_id: str) -> None:
        """
        Apply label to a message.

        Args:
            message_id: Gmail message ID
        """
        if not self.label_id:
            return

        try:
            self.service.users().messages().modify(
                userId='me',
                id=message_id,
                body={'addLabelIds': [self.label_id]}
            ).execute()

            if self.verbose:
                print(f"Applied label '{GMAIL_LABEL_NAME}' to message {message_id}")

        except Exception as e:
            # Don't fail if label application fails, just log warning
            print(f"Warning: Failed to apply label: {str(e)}")


class MockGmailClient:
    """Mock Gmail client for testing without actual API calls."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.drafts_created = []
        self.emails_sent = []

    def create_draft(self, to: str, subject: str, html_body: str, plain_body: Optional[str] = None) -> str:
        """Mock draft creation."""
        draft_id = f"mock_draft_{len(self.drafts_created) + 1}"
        self.drafts_created.append({
            'id': draft_id,
            'to': to,
            'subject': subject,
            'html_body': html_body,
        })
        if self.verbose:
            print(f"[MOCK] Created draft {draft_id} to {to}")
        return draft_id

    def send_email(self, to: str, subject: str, html_body: str, plain_body: Optional[str] = None) -> str:
        """Mock email sending."""
        message_id = f"mock_message_{len(self.emails_sent) + 1}"
        self.emails_sent.append({
            'id': message_id,
            'to': to,
            'subject': subject,
            'html_body': html_body,
        })
        if self.verbose:
            print(f"[MOCK] Sent email {message_id} to {to}")
        return message_id
