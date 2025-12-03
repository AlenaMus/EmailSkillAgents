"""
URL Extraction Module

This module extracts URLs from email bodies (both plain text and HTML).
Supports multiple URL formats and handles various edge cases.
"""

import re
from typing import List, Set
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class URLExtractor:
    """Extract URLs from email content"""

    # Comprehensive URL regex pattern
    URL_PATTERN = re.compile(
        r'http[s]?://'  # http:// or https://
        r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # domain and path
    )

    def __init__(self):
        """Initialize URL extractor"""
        pass

    def extract_from_text(self, text: str) -> List[str]:
        """
        Extract URLs from plain text

        Args:
            text: Plain text content

        Returns:
            List of extracted URLs
        """
        if not text:
            return []

        urls = self.URL_PATTERN.findall(text)
        return self._clean_urls(urls)

    def extract_from_html(self, html: str) -> List[str]:
        """
        Extract URLs from HTML content

        Args:
            html: HTML content

        Returns:
            List of extracted URLs
        """
        if not html:
            return []

        urls = []

        try:
            soup = BeautifulSoup(html, 'html.parser')

            # Extract from anchor tags
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith(('http://', 'https://')):
                    urls.append(href)

            # Also check for URLs in plain text within HTML
            text = soup.get_text()
            text_urls = self.extract_from_text(text)
            urls.extend(text_urls)

        except Exception as e:
            print(f"Warning: Error parsing HTML: {e}")
            # Fallback to regex on raw HTML
            urls = self.extract_from_text(html)

        return self._clean_urls(urls)

    def extract_from_email(self, body_plain: str, body_html: str) -> List[str]:
        """
        Extract URLs from email body (tries HTML first, then plain text)

        Args:
            body_plain: Plain text email body
            body_html: HTML email body

        Returns:
            List of unique URLs found
        """
        urls = []

        # Try HTML first (more reliable for links)
        if body_html:
            urls.extend(self.extract_from_html(body_html))

        # Also check plain text if available
        if body_plain:
            urls.extend(self.extract_from_text(body_plain))

        # Remove duplicates while preserving order
        return self._deduplicate_urls(urls)

    def _clean_urls(self, urls: List[str]) -> List[str]:
        """
        Clean and validate URLs

        Args:
            urls: List of raw URLs

        Returns:
            List of cleaned URLs
        """
        cleaned = []

        for url in urls:
            # Remove trailing punctuation and whitespace
            url = url.rstrip('.,;:!?)')
            url = url.strip()

            # Validate URL
            if self._is_valid_url(url):
                cleaned.append(url)

        return cleaned

    def _is_valid_url(self, url: str) -> bool:
        """
        Validate URL format

        Args:
            url: URL string

        Returns:
            True if valid, False otherwise
        """
        try:
            result = urlparse(url)
            return all([result.scheme in ('http', 'https'), result.netloc])
        except Exception:
            return False

    def _deduplicate_urls(self, urls: List[str]) -> List[str]:
        """
        Remove duplicate URLs while preserving order

        Args:
            urls: List of URLs (may contain duplicates)

        Returns:
            List of unique URLs
        """
        seen: Set[str] = set()
        unique = []

        for url in urls:
            if url not in seen:
                seen.add(url)
                unique.append(url)

        return unique


def extract_urls_from_emails(emails: List[dict]) -> List[dict]:
    """
    Extract URLs from a list of email dictionaries

    Args:
        emails: List of email dictionaries with 'body_plain' and 'body_html' keys

    Returns:
        List of email dictionaries with added 'urls' key
    """
    extractor = URLExtractor()

    for email in emails:
        body_plain = email.get('body_plain', '')
        body_html = email.get('body_html', '')

        urls = extractor.extract_from_email(body_plain, body_html)
        email['urls'] = urls

    return emails


def format_urls_for_excel(urls: List[str]) -> str:
    """
    Format URLs for Excel cell (comma-separated)

    Args:
        urls: List of URLs

    Returns:
        Comma-separated string of URLs
    """
    if not urls:
        return ''

    return ', '.join(urls)
