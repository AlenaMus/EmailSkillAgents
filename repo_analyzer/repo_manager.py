"""
Repository manager for cloning and managing Git repositories.
"""

import os
import shutil
import time
import re
from pathlib import Path
from typing import Tuple, Optional
import tempfile
from datetime import datetime

try:
    import git
    from git import Repo, GitCommandError
except ImportError:
    raise ImportError("GitPython is required. Install with: pip install GitPython")

from .config import CLONE_TIMEOUT, RETRY_ATTEMPTS, RETRY_BACKOFF_BASE, TEMP_DIR_PREFIX
from .errors import (
    RepositoryNotFoundError,
    RepositoryTimeoutError,
    RepositoryAccessDeniedError,
    InvalidURLError,
    NetworkError
)


class RepositoryManager:
    """Manage repository cloning and cleanup."""

    def __init__(self, temp_dir: Optional[str] = None):
        """
        Initialize repository manager.

        Args:
            temp_dir: Custom temporary directory path. If None, creates one automatically.
        """
        if temp_dir is None:
            # Create temp directory with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.temp_dir = Path(tempfile.gettempdir()) / f"{TEMP_DIR_PREFIX}{timestamp}"
        else:
            self.temp_dir = Path(temp_dir)

        # Create temp directory if it doesn't exist
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.clone_count = 0

    def clone(self, url: str) -> Tuple[Optional[str], bool, str]:
        """
        Clone a GitHub repository with retries.

        Args:
            url: GitHub repository URL (HTTPS)

        Returns:
            Tuple of (local_path, success, error_message)
            - local_path: Path to cloned repository (None if failed)
            - success: True if clone succeeded
            - error_message: Error message if failed (empty string if success)
        """
        # Validate URL
        if not self._is_valid_github_url(url):
            return None, False, "Invalid GitHub URL format"

        # Extract repo name for directory
        repo_name = self._extract_repo_name(url)
        if not repo_name:
            return None, False, "Could not extract repository name from URL"

        # Create local path
        self.clone_count += 1
        local_path = self.temp_dir / f"repo_{self.clone_count}_{repo_name}"

        # Clone with retries
        for attempt in range(1, RETRY_ATTEMPTS + 1):
            try:
                success, error = self._clone_once(url, local_path)

                if success:
                    return str(local_path), True, ""

                # Check if we should retry
                if not self._should_retry(error) or attempt == RETRY_ATTEMPTS:
                    return None, False, error

                # Exponential backoff
                backoff_time = RETRY_BACKOFF_BASE ** attempt
                print(f"  Retry {attempt}/{RETRY_ATTEMPTS} in {backoff_time}s...")
                time.sleep(backoff_time)

            except Exception as e:
                error = str(e)

                if attempt == RETRY_ATTEMPTS:
                    return None, False, f"Clone failed after {RETRY_ATTEMPTS} attempts: {error}"

                backoff_time = RETRY_BACKOFF_BASE ** attempt
                time.sleep(backoff_time)

        return None, False, f"Clone failed after {RETRY_ATTEMPTS} attempts"

    def _clone_once(self, url: str, local_path: Path) -> Tuple[bool, str]:
        """
        Attempt to clone repository once.

        Args:
            url: Repository URL
            local_path: Local destination path

        Returns:
            Tuple of (success, error_message)
        """
        try:
            # Remove existing directory if present
            if local_path.exists():
                shutil.rmtree(local_path)

            # Clone with shallow depth for speed
            # Note: GitPython's timeout parameter doesn't work reliably on Windows
            # So we just clone without timeout for now
            Repo.clone_from(
                url,
                local_path,
                depth=1  # Shallow clone
            )

            return True, ""

        except GitCommandError as e:
            error_msg = str(e).lower()

            # Parse error type
            if '404' in error_msg or 'not found' in error_msg or 'repository not found' in error_msg:
                return False, "Repository not found or deleted"
            elif '403' in error_msg or 'forbidden' in error_msg:
                return False, "Private repository - access denied"
            elif 'timeout' in error_msg:
                return False, "Clone timeout (>5 min)"
            elif 'network' in error_msg or 'connection' in error_msg:
                return False, "Network connection failed"
            else:
                return False, f"Git error: {str(e)}"

        except Exception as e:
            return False, f"Unexpected error: {str(e)}"

    def _is_valid_github_url(self, url: str) -> bool:
        """
        Validate GitHub URL format.

        Args:
            url: URL to validate

        Returns:
            True if valid GitHub URL
        """
        # Accept various GitHub URL formats
        patterns = [
            r'^https?://github\.com/[\w\-]+/[\w\-\.]+/?$',
            r'^https?://github\.com/[\w\-]+/[\w\-\.]+\.git$',
            r'^git@github\.com:[\w\-]+/[\w\-\.]+\.git$'
        ]

        for pattern in patterns:
            if re.match(pattern, url.strip()):
                return True

        return False

    def _extract_repo_name(self, url: str) -> Optional[str]:
        """
        Extract repository name from URL.

        Args:
            url: GitHub URL

        Returns:
            Repository name or None if extraction fails
        """
        try:
            # Remove trailing slashes and .git
            url = url.strip().rstrip('/').rstrip('.git')

            # Extract last part of URL
            parts = url.split('/')
            if len(parts) >= 2:
                return parts[-1]

            return None
        except:
            return None

    def _should_retry(self, error: str) -> bool:
        """
        Determine if error is transient and should be retried.

        Args:
            error: Error message

        Returns:
            True if error is transient
        """
        transient_errors = [
            'timeout',
            'network',
            'connection',
            'temporary'
        ]

        error_lower = error.lower()

        for transient in transient_errors:
            if transient in error_lower:
                return True

        return False

    def cleanup(self):
        """
        Remove temporary directory and all cloned repositories.
        """
        try:
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                print(f"Cleaned up temporary directory: {self.temp_dir}")
        except Exception as e:
            print(f"Warning: Could not clean up temporary directory: {e}")

    def get_temp_dir(self) -> str:
        """Get the temporary directory path."""
        return str(self.temp_dir)
