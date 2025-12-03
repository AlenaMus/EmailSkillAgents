"""
Command-Line Interface Module

This module provides the CLI interface for GmailAgent using Click.
Handles all user commands and orchestrates the email export workflow.
"""

import sys
from pathlib import Path
from typing import Optional

import click

from .auth import GmailAuthenticator, setup_credentials
from .gmail_client import GmailClient
from .url_extractor import extract_urls_from_emails
from .excel_exporter import export_emails_to_excel


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    GmailAgent - Gmail Email Exporter

    Retrieve emails from Gmail using filters and export them to Excel with URL extraction.
    All exports are saved to the ./exports/ directory with smart filenames.
    """
    pass


@cli.command()
@click.option('--credentials', type=click.Path(exists=True), help='Path to OAuth credentials JSON file')
def auth(credentials: Optional[str]):
    """
    Authenticate with Gmail API using OAuth 2.0

    This command will open a browser window for you to authorize the application.
    Your credentials will be saved securely for future use.
    """
    click.echo("=" * 60)
    click.echo("GmailAgent - Gmail API Authentication")
    click.echo("=" * 60)
    click.echo()

    try:
        if credentials:
            # Copy credentials to default location
            click.echo(f"Setting up credentials from: {credentials}")
            if setup_credentials(credentials):
                click.echo()
                click.echo("Credentials setup complete!")
            else:
                click.echo("Error: Failed to set up credentials.", err=True)
                sys.exit(1)

        # Authenticate
        authenticator = GmailAuthenticator()

        if authenticator.is_authenticated():
            click.echo("You are already authenticated!")
            click.echo()
            reauth = click.confirm("Do you want to re-authenticate?", default=False)
            if not reauth:
                click.echo("Using existing credentials.")
                return

        click.echo("Starting authentication process...")
        click.echo()
        authenticator.authenticate()

        click.echo()
        click.echo("[OK] Authentication successful!")
        click.echo("You can now use 'gmailagent export' to retrieve emails.")

    except FileNotFoundError as e:
        click.echo()
        click.echo("Error: " + str(e), err=True)
        click.echo()
        click.echo("Please follow these steps:")
        click.echo("1. Go to Google Cloud Console: https://console.cloud.google.com/")
        click.echo("2. Create a new project or select existing one")
        click.echo("3. Enable Gmail API for your project")
        click.echo("4. Create OAuth 2.0 credentials (Desktop application)")
        click.echo("5. Download the credentials JSON file")
        click.echo("6. Run: gmailagent auth --credentials /path/to/credentials.json")
        sys.exit(1)

    except Exception as e:
        click.echo()
        click.echo(f"Error: Authentication failed: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--folder', help='Filter by Gmail folder (e.g., INBOX, SENT, IMPORTANT)')
@click.option('--label', help='Filter by Gmail label')
@click.option('--tag', help='Filter by Gmail tag (synonym for label)')
@click.option('--from', 'from_email', help='Filter by sender email or name')
@click.option('--to', 'to_email', help='Filter by recipient email or name')
@click.option('--subject', help='Filter by subject (contains text)')
@click.option('--after', help='Filter emails after date (YYYY-MM-DD or YYYY/MM/DD)')
@click.option('--before', help='Filter emails before date (YYYY-MM-DD or YYYY/MM/DD)')
@click.option('--newer-than', help='Filter emails newer than (e.g., 7d for 7 days, 2m for 2 months)')
@click.option('--older-than', help='Filter emails older than (e.g., 7d for 7 days, 2m for 2 months)')
@click.option('--output', type=click.Path(), help='Custom output file path (overrides auto-naming)')
@click.option('--limit', default=1000, help='Maximum number of emails to retrieve (default: 1000)')
def export(folder, label, tag, from_email, to_email, subject, after, before, newer_than, older_than, output, limit):
    """
    Export emails to Excel with URL extraction

    Retrieves emails from Gmail based on specified filters and exports them
    to an Excel file with smart filename generation.

    Examples:
      gmailagent export --label "Work"
      gmailagent export --folder "INBOX" --from "boss@company.com"
      gmailagent export --tag "clients" --subject "invoice"
      gmailagent export --label "Important" --output custom.xlsx
      gmailagent export --label "homework" --after "2025-11-01"
      gmailagent export --subject "Assignment" --newer-than "7d"
      gmailagent export --label "homework" --subject "Lesson 19" --after "2025-12-01"
    """
    click.echo("=" * 60)
    click.echo("GmailAgent - Email Export")
    click.echo("=" * 60)
    click.echo()

    # Check if at least one filter is specified
    if not any([folder, label, tag, from_email, to_email, subject, after, before, newer_than, older_than]):
        click.echo("Warning: No filters specified. Exporting all emails (up to limit).")
        click.echo()
        proceed = click.confirm("Do you want to continue?", default=False)
        if not proceed:
            click.echo("Export cancelled.")
            return

    try:
        # Authenticate
        click.echo("Authenticating with Gmail API...")
        authenticator = GmailAuthenticator()
        service = authenticator.get_service()
        click.echo("[OK] Authenticated successfully")
        click.echo()

        # Initialize Gmail client
        client = GmailClient(service)

        # Get active filters
        filters = client.get_active_filters(
            folder=folder,
            label=label,
            tag=tag,
            from_email=from_email,
            to_email=to_email,
            subject=subject,
            after=after,
            before=before,
            newer_than=newer_than,
            older_than=older_than
        )

        # Display active filters
        if filters:
            click.echo("Active filters:")
            for key, value in filters.items():
                click.echo(f"  - {key}: {value}")
            click.echo()

        # Retrieve emails
        click.echo(f"Retrieving emails (max: {limit})...")
        emails = client.retrieve_emails(
            folder=folder,
            label=label,
            tag=tag,
            from_email=from_email,
            to_email=to_email,
            subject=subject,
            after=after,
            before=before,
            newer_than=newer_than,
            older_than=older_than,
            max_results=limit
        )

        if not emails:
            click.echo()
            click.echo("No emails found matching the specified filters.")
            return

        click.echo(f"[OK] Retrieved {len(emails)} emails")
        click.echo()

        # Extract URLs
        click.echo("Extracting URLs from email bodies...")
        emails = extract_urls_from_emails(emails)

        # Count emails with URLs
        emails_with_urls = sum(1 for email in emails if email.get('urls'))
        total_urls = sum(len(email.get('urls', [])) for email in emails)
        click.echo(f"[OK] Extracted {total_urls} URLs from {emails_with_urls} emails")
        click.echo()

        # Export to Excel
        click.echo("Generating Excel file...")
        output_file = export_emails_to_excel(
            emails=emails,
            filters=filters,
            output_path=output
        )
        click.echo(f"[OK] Excel file created")
        click.echo()

        # Display results
        click.echo("=" * 60)
        click.echo(f"[OK] Exported {len(emails)} emails to: {output_file}")
        click.echo("=" * 60)

    except FileNotFoundError as e:
        click.echo()
        click.echo("Error: Not authenticated.", err=True)
        click.echo("Please run 'gmailagent auth' first to authenticate with Gmail.")
        sys.exit(1)

    except Exception as e:
        click.echo()
        click.echo(f"Error: Export failed: {e}", err=True)
        import traceback
        if '--debug' in sys.argv:
            traceback.print_exc()
        sys.exit(1)


@cli.command()
def list_labels():
    """
    List all available Gmail labels

    Shows all labels in your Gmail account, including system labels
    (INBOX, SENT, etc.) and custom labels.
    """
    click.echo("=" * 60)
    click.echo("GmailAgent - List Labels")
    click.echo("=" * 60)
    click.echo()

    try:
        # Authenticate
        authenticator = GmailAuthenticator()
        service = authenticator.get_service()

        # Get labels
        client = GmailClient(service)
        labels = client.list_labels()

        if not labels:
            click.echo("No labels found.")
            return

        # Separate system and user labels
        system_labels = []
        user_labels = []

        for label in labels:
            label_type = label.get('type', '')
            if label_type == 'system':
                system_labels.append(label)
            else:
                user_labels.append(label)

        # Display system labels
        if system_labels:
            click.echo("System Labels:")
            for label in sorted(system_labels, key=lambda x: x['name']):
                click.echo(f"  - {label['name']}")
            click.echo()

        # Display user labels
        if user_labels:
            click.echo("Custom Labels:")
            for label in sorted(user_labels, key=lambda x: x['name']):
                click.echo(f"  - {label['name']}")
            click.echo()

        click.echo(f"Total: {len(labels)} labels")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command()
def list_folders():
    """
    List common Gmail folders (system labels)

    Shows commonly used Gmail folders that can be used with --folder flag.
    """
    click.echo("=" * 60)
    click.echo("GmailAgent - Gmail Folders")
    click.echo("=" * 60)
    click.echo()

    folders = [
        "INBOX",
        "SENT",
        "DRAFT",
        "SPAM",
        "TRASH",
        "IMPORTANT",
        "STARRED",
        "UNREAD",
    ]

    click.echo("Available Gmail folders:")
    for folder in folders:
        click.echo(f"  - {folder}")
    click.echo()
    click.echo("Usage: gmailagent export --folder INBOX")


@cli.command()
def revoke():
    """
    Revoke authentication and remove stored credentials

    This will remove your saved credentials and you will need to
    re-authenticate to use GmailAgent.
    """
    click.echo("=" * 60)
    click.echo("GmailAgent - Revoke Authentication")
    click.echo("=" * 60)
    click.echo()

    confirm = click.confirm(
        "Are you sure you want to revoke authentication?",
        default=False
    )

    if not confirm:
        click.echo("Cancelled.")
        return

    try:
        authenticator = GmailAuthenticator()
        success = authenticator.revoke_credentials()

        if success:
            click.echo()
            click.echo("[OK] Authentication revoked successfully")
            click.echo("Run 'gmailagent auth' to re-authenticate.")
        else:
            click.echo()
            click.echo("No credentials found to revoke.")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command()
def info():
    """
    Display GmailAgent information and status
    """
    click.echo("=" * 60)
    click.echo("GmailAgent v1.0.0")
    click.echo("=" * 60)
    click.echo()
    click.echo("Gmail Email Exporter with URL Extraction")
    click.echo()

    # Check authentication status
    try:
        authenticator = GmailAuthenticator()
        if authenticator.is_authenticated():
            click.echo("Authentication: [OK] Authenticated")
        else:
            click.echo("Authentication: [ERROR] Not authenticated")
            click.echo("  Run 'gmailagent auth' to authenticate")
    except Exception:
        click.echo("Authentication: [ERROR] Not authenticated")

    click.echo()
    click.echo("Exports Directory: ./exports/")

    # Check if exports directory exists
    exports_dir = Path("./exports")
    if exports_dir.exists():
        files = list(exports_dir.glob("*.xlsx"))
        click.echo(f"Exported Files: {len(files)}")
    else:
        click.echo("Exported Files: 0")

    click.echo()
    click.echo("For help: gmailagent --help")
    click.echo("Documentation: https://github.com/yourusername/gmailagent")


if __name__ == '__main__':
    cli()
