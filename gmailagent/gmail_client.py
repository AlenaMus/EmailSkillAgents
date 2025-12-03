"""
Gmail API Client Module

This module provides a wrapper around the Gmail API for retrieving
emails with various filters and parsing email content.
"""

import base64
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import List, Dict, Optional, Any

from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError


class GmailClient:
    """Gmail API client wrapper for email retrieval and filtering"""

    def __init__(self, service: Resource):
        """
        Initialize Gmail client

        Args:
            service: Authenticated Gmail API service object
        """
        self.service = service

    def list_labels(self) -> List[Dict[str, str]]:
        """
        Get all Gmail labels for the user

        Returns:
            List of label dictionaries with 'id' and 'name'
        """
        try:
            results = self.service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])
            return labels
        except HttpError as error:
            print(f"Error retrieving labels: {error}")
            return []

    def build_query(
        self,
        folder: Optional[str] = None,
        label: Optional[str] = None,
        tag: Optional[str] = None,
        from_email: Optional[str] = None,
        to_email: Optional[str] = None,
        subject: Optional[str] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
        newer_than: Optional[str] = None,
        older_than: Optional[str] = None,
    ) -> str:
        """
        Build Gmail search query from filters

        Args:
            folder: Gmail folder name (maps to system labels like INBOX, SENT, etc.)
            label: Gmail label name
            tag: Gmail tag (synonym for label)
            from_email: Sender email or name
            to_email: Recipient email or name
            subject: Subject text to search for
            after: Date filter for emails after date (YYYY-MM-DD or YYYY/MM/DD)
            before: Date filter for emails before date (YYYY-MM-DD or YYYY/MM/DD)
            newer_than: Relative date filter (e.g., 7d, 2m, 1y)
            older_than: Relative date filter (e.g., 7d, 2m, 1y)

        Returns:
            Gmail search query string
        """
        query_parts = []

        # Handle folder (system labels)
        if folder:
            # Map common folder names to Gmail labels
            folder_upper = folder.upper()
            if folder_upper in ['INBOX', 'SENT', 'DRAFT', 'SPAM', 'TRASH', 'IMPORTANT', 'STARRED']:
                query_parts.append(f'in:{folder_upper}')
            else:
                # Treat as regular label
                query_parts.append(f'label:{folder}')

        # Handle label
        if label:
            query_parts.append(f'label:{label}')

        # Handle tag (same as label)
        if tag:
            query_parts.append(f'label:{tag}')

        # Handle from
        if from_email:
            query_parts.append(f'from:{from_email}')

        # Handle to
        if to_email:
            query_parts.append(f'to:{to_email}')

        # Handle subject
        if subject:
            query_parts.append(f'subject:{subject}')

        # Handle date filters
        if after:
            # Convert YYYY-MM-DD to YYYY/MM/DD for Gmail
            date_str = after.replace('-', '/')
            query_parts.append(f'after:{date_str}')

        if before:
            # Convert YYYY-MM-DD to YYYY/MM/DD for Gmail
            date_str = before.replace('-', '/')
            query_parts.append(f'before:{date_str}')

        if newer_than:
            query_parts.append(f'newer_than:{newer_than}')

        if older_than:
            query_parts.append(f'older_than:{older_than}')

        return ' '.join(query_parts) if query_parts else ''

    def get_messages(
        self,
        query: str = '',
        max_results: int = 1000,
        include_spam_trash: bool = False
    ) -> List[str]:
        """
        Get list of message IDs matching the query

        Args:
            query: Gmail search query
            max_results: Maximum number of messages to retrieve
            include_spam_trash: Whether to include spam and trash

        Returns:
            List of message IDs
        """
        message_ids = []

        try:
            page_token = None
            while len(message_ids) < max_results:
                results = self.service.users().messages().list(
                    userId='me',
                    q=query,
                    maxResults=min(500, max_results - len(message_ids)),
                    pageToken=page_token,
                    includeSpamTrash=include_spam_trash
                ).execute()

                messages = results.get('messages', [])
                if not messages:
                    break

                message_ids.extend([msg['id'] for msg in messages])

                page_token = results.get('nextPageToken')
                if not page_token:
                    break

        except HttpError as error:
            print(f"Error retrieving messages: {error}")

        return message_ids[:max_results]

    def get_message_details(self, message_id: str) -> Optional[Dict[str, Any]]:
        """
        Get full details of a single message

        Args:
            message_id: Gmail message ID

        Returns:
            Dictionary with message details or None on error
        """
        try:
            message = self.service.users().messages().get(
                userId='me',
                id=message_id,
                format='full'
            ).execute()

            return self._parse_message(message)

        except HttpError as error:
            print(f"Error retrieving message {message_id}: {error}")
            return None

    def _parse_message(self, message: Dict) -> Dict[str, Any]:
        """
        Parse Gmail message into structured format

        Args:
            message: Raw Gmail API message object

        Returns:
            Parsed message dictionary
        """
        headers = message.get('payload', {}).get('headers', [])

        # Extract common headers
        subject = self._get_header(headers, 'Subject')
        from_email = self._get_header(headers, 'From')
        to_email = self._get_header(headers, 'To')
        date_str = self._get_header(headers, 'Date')

        # Parse date
        date = None
        if date_str:
            try:
                date = parsedate_to_datetime(date_str)
            except Exception:
                # Fallback to internal date
                internal_date = message.get('internalDate')
                if internal_date:
                    date = datetime.fromtimestamp(int(internal_date) / 1000)

        # Extract body
        body = self._get_message_body(message.get('payload', {}))

        return {
            'id': message['id'],
            'thread_id': message.get('threadId'),
            'subject': subject or '(No Subject)',
            'from': from_email or '',
            'to': to_email or '',
            'date': date or datetime.now(),
            'body_plain': body.get('plain', ''),
            'body_html': body.get('html', ''),
            'snippet': message.get('snippet', ''),
        }

    def _get_header(self, headers: List[Dict], name: str) -> Optional[str]:
        """Get header value by name"""
        for header in headers:
            if header.get('name', '').lower() == name.lower():
                return header.get('value')
        return None

    def _get_message_body(self, payload: Dict) -> Dict[str, str]:
        """
        Extract message body from payload

        Args:
            payload: Message payload from Gmail API

        Returns:
            Dictionary with 'plain' and 'html' body content
        """
        body = {'plain': '', 'html': ''}

        # Check for direct body data
        if 'body' in payload and 'data' in payload['body']:
            mime_type = payload.get('mimeType', '')
            data = payload['body']['data']
            decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')

            if 'text/plain' in mime_type:
                body['plain'] = decoded
            elif 'text/html' in mime_type:
                body['html'] = decoded

        # Check parts for multipart messages
        if 'parts' in payload:
            for part in payload['parts']:
                self._extract_part_body(part, body)

        return body

    def _extract_part_body(self, part: Dict, body: Dict[str, str]):
        """
        Recursively extract body from message parts

        Args:
            part: Message part from Gmail API
            body: Dictionary to store extracted body
        """
        mime_type = part.get('mimeType', '')

        # Extract body data
        if 'body' in part and 'data' in part['body']:
            data = part['body']['data']
            decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')

            if mime_type == 'text/plain':
                body['plain'] += decoded
            elif mime_type == 'text/html':
                body['html'] += decoded

        # Recurse into nested parts
        if 'parts' in part:
            for subpart in part['parts']:
                self._extract_part_body(subpart, body)

    def retrieve_emails(
        self,
        folder: Optional[str] = None,
        label: Optional[str] = None,
        tag: Optional[str] = None,
        from_email: Optional[str] = None,
        to_email: Optional[str] = None,
        subject: Optional[str] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
        newer_than: Optional[str] = None,
        older_than: Optional[str] = None,
        max_results: int = 1000,
        progress_callback: Optional[callable] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve emails with filters

        Args:
            folder: Gmail folder name
            label: Gmail label name
            tag: Gmail tag
            from_email: Sender email or name
            to_email: Recipient email or name
            subject: Subject text
            after: Date filter for emails after date
            before: Date filter for emails before date
            newer_than: Relative date filter
            older_than: Relative date filter
            max_results: Maximum number of emails
            progress_callback: Optional callback function for progress updates

        Returns:
            List of email dictionaries
        """
        # Build search query
        query = self.build_query(
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

        print(f"Search query: {query if query else '(all emails)'}")

        # Get message IDs
        print("Fetching message IDs...")
        message_ids = self.get_messages(query, max_results)

        if not message_ids:
            print("No messages found matching filters.")
            return []

        print(f"Found {len(message_ids)} messages. Retrieving details...")

        # Retrieve message details
        emails = []
        total = len(message_ids)

        for idx, msg_id in enumerate(message_ids, 1):
            email = self.get_message_details(msg_id)
            if email:
                emails.append(email)

            # Progress callback
            if progress_callback:
                progress_callback(idx, total)
            elif idx % 10 == 0 or idx == total:
                print(f"Processing: {idx}/{total} emails...")

        return emails

    def get_active_filters(
        self,
        folder: Optional[str] = None,
        label: Optional[str] = None,
        tag: Optional[str] = None,
        from_email: Optional[str] = None,
        to_email: Optional[str] = None,
        subject: Optional[str] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
        newer_than: Optional[str] = None,
        older_than: Optional[str] = None,
    ) -> Dict[str, str]:
        """
        Get dictionary of active filters for filename generation

        Args:
            folder: Gmail folder name
            label: Gmail label name
            tag: Gmail tag
            from_email: Sender email or name
            to_email: Recipient email or name
            subject: Subject text
            after: Date filter for emails after date
            before: Date filter for emails before date
            newer_than: Relative date filter
            older_than: Relative date filter

        Returns:
            Dictionary of active filters
        """
        filters = {}

        if folder:
            filters['folder'] = folder
        if label:
            filters['label'] = label
        if tag:
            filters['tag'] = tag
        if from_email:
            filters['from'] = from_email
        if to_email:
            filters['to'] = to_email
        if subject:
            filters['subject'] = subject
        if after:
            filters['after'] = after
        if before:
            filters['before'] = before
        if newer_than:
            filters['newer_than'] = newer_than
        if older_than:
            filters['older_than'] = older_than

        return filters
