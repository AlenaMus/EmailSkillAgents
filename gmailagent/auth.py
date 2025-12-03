"""
Gmail OAuth 2.0 Authentication Module

This module handles OAuth 2.0 authentication with Gmail API,
including credential storage, token refresh, and secure access.
"""

import os
import pickle
from pathlib import Path
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API scope - readonly access only
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Default paths for credentials storage
DEFAULT_CONFIG_DIR = Path.home() / '.gmailagent'
DEFAULT_CREDENTIALS_FILE = DEFAULT_CONFIG_DIR / 'credentials.json'
DEFAULT_TOKEN_FILE = DEFAULT_CONFIG_DIR / 'token.pickle'


class GmailAuthenticator:
    """Handles Gmail API OAuth 2.0 authentication"""

    def __init__(self, credentials_path: Optional[str] = None, token_path: Optional[str] = None):
        """
        Initialize the authenticator

        Args:
            credentials_path: Path to OAuth client credentials JSON file
            token_path: Path to store/load the token pickle file
        """
        self.credentials_path = Path(credentials_path) if credentials_path else DEFAULT_CREDENTIALS_FILE
        self.token_path = Path(token_path) if token_path else DEFAULT_TOKEN_FILE
        self.creds: Optional[Credentials] = None

        # Ensure config directory exists
        DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    def authenticate(self) -> Credentials:
        """
        Authenticate with Gmail API using OAuth 2.0

        Returns:
            Credentials object for Gmail API access

        Raises:
            FileNotFoundError: If credentials file not found
            Exception: For authentication errors
        """
        # Load existing token if available
        if self.token_path.exists():
            try:
                with open(self.token_path, 'rb') as token:
                    self.creds = pickle.load(token)
            except Exception as e:
                print(f"Warning: Could not load token file: {e}")
                self.creds = None

        # Refresh or get new credentials if needed
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    print("Refreshing expired credentials...")
                    self.creds.refresh(Request())
                except Exception as e:
                    print(f"Could not refresh token: {e}")
                    self.creds = None

            # Get new credentials through OAuth flow
            if not self.creds:
                if not self.credentials_path.exists():
                    raise FileNotFoundError(
                        f"Credentials file not found at {self.credentials_path}\n"
                        f"Please download OAuth credentials from Google Cloud Console and save to:\n"
                        f"{self.credentials_path}"
                    )

                print("Starting OAuth 2.0 authentication flow...")
                print("A browser window will open for you to authorize the application.")

                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES
                )
                self.creds = flow.run_local_server(port=0)

                print("Authentication successful!")

            # Save credentials for future use
            try:
                with open(self.token_path, 'wb') as token:
                    pickle.dump(self.creds, token)
                # Set restrictive permissions (Unix-like systems)
                try:
                    os.chmod(self.token_path, 0o600)
                except Exception:
                    pass  # Windows doesn't support chmod
            except Exception as e:
                print(f"Warning: Could not save token file: {e}")

        return self.creds

    def get_service(self):
        """
        Get authenticated Gmail API service

        Returns:
            Gmail API service object
        """
        creds = self.authenticate()
        service = build('gmail', 'v1', credentials=creds)
        return service

    def is_authenticated(self) -> bool:
        """
        Check if valid credentials exist

        Returns:
            True if authenticated, False otherwise
        """
        if self.token_path.exists():
            try:
                with open(self.token_path, 'rb') as token:
                    creds = pickle.load(token)
                return creds and creds.valid
            except Exception:
                return False
        return False

    def revoke_credentials(self) -> bool:
        """
        Revoke and remove stored credentials

        Returns:
            True if successful, False otherwise
        """
        try:
            if self.token_path.exists():
                self.token_path.unlink()
                print("Credentials removed successfully.")
                return True
            else:
                print("No credentials found to remove.")
                return False
        except Exception as e:
            print(f"Error removing credentials: {e}")
            return False


def setup_credentials(credentials_json_path: str) -> bool:
    """
    Helper function to copy OAuth credentials to default location

    Args:
        credentials_json_path: Path to the downloaded credentials JSON

    Returns:
        True if successful, False otherwise
    """
    try:
        source = Path(credentials_json_path)
        if not source.exists():
            print(f"Error: File not found: {credentials_json_path}")
            return False

        # Create config directory
        DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

        # Copy credentials file
        import shutil
        shutil.copy(source, DEFAULT_CREDENTIALS_FILE)

        print(f"Credentials copied to: {DEFAULT_CREDENTIALS_FILE}")
        print("You can now run 'gmailagent auth' to authenticate.")
        return True
    except Exception as e:
        print(f"Error setting up credentials: {e}")
        return False
