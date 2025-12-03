"""
Code metrics calculator for Repository Analyzer Agent.
Calculates lines of code, file counts, and grades.
"""

import os
from pathlib import Path
from typing import Dict, Tuple
from .config import CODE_EXTENSIONS, EXCLUDE_DIRS, LINE_LIMIT
from .errors import MetricsCalculationError


class MetricsCalculator:
    """Calculate code metrics and grade for a repository."""

    def __init__(self):
        """Initialize metrics calculator."""
        self.code_extensions = [ext.lower() for ext in CODE_EXTENSIONS]
        self.exclude_dirs = set(EXCLUDE_DIRS)
        self.line_limit = LINE_LIMIT

    def calculate(self, repo_path: str) -> Dict:
        """
        Calculate metrics for a repository.

        Args:
            repo_path: Path to the cloned repository

        Returns:
            Dict with keys: total_lines, total_files, files_under_130, grade

        Raises:
            MetricsCalculationError: If calculation fails
        """
        try:
            repo_path = Path(repo_path)

            if not repo_path.exists():
                raise MetricsCalculationError(f"Repository path does not exist: {repo_path}")

            total_lines = 0
            total_files = 0
            files_under_limit = 0

            # Traverse directory tree
            for file_path in self._traverse_code_files(repo_path):
                try:
                    line_count = self._count_lines(file_path)
                    total_lines += line_count
                    total_files += 1

                    if line_count < self.line_limit:
                        files_under_limit += 1

                except Exception as e:
                    # Skip files that can't be read, but log warning
                    print(f"Warning: Could not read file {file_path}: {e}")
                    continue

            # Calculate grade
            grade = self._calculate_grade(files_under_limit, total_files)

            return {
                'total_lines': total_lines,
                'total_files': total_files,
                'files_under_130': files_under_limit,
                'grade': grade
            }

        except Exception as e:
            if isinstance(e, MetricsCalculationError):
                raise
            raise MetricsCalculationError(f"Metrics calculation failed: {str(e)}")

    def _traverse_code_files(self, repo_path: Path):
        """
        Traverse repository and yield code file paths.

        Args:
            repo_path: Path to repository

        Yields:
            Path objects for code files
        """
        for root, dirs, files in os.walk(repo_path):
            # Remove excluded directories from traversal
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]

            # Check each file
            for file in files:
                file_path = Path(root) / file

                if self._is_code_file(file_path):
                    yield file_path

    def _is_code_file(self, file_path: Path) -> bool:
        """
        Check if a file is a code file (not config, docs, or binary).

        Args:
            file_path: Path to file

        Returns:
            True if file is a code file
        """
        # Check extension
        extension = file_path.suffix.lower()

        if extension not in self.code_extensions:
            return False

        # Exclude certain file patterns
        filename = file_path.name.lower()

        # Exclude config files
        config_patterns = [
            'package.json', 'package-lock.json',
            'requirements.txt', 'gemfile', 'gemfile.lock',
            '.gitignore', '.env', '.env.local',
            'readme', 'license', 'changelog'
        ]

        for pattern in config_patterns:
            if pattern in filename:
                return False

        # Exclude compiled files
        if extension in ['.pyc', '.class', '.exe', '.dll', '.so']:
            return False

        return True

    def _count_lines(self, file_path: Path) -> int:
        """
        Count non-empty lines in a file.

        According to PRD: Count only non-empty lines (strip whitespace, skip if empty).
        Include comment lines (they're still code maintenance).

        Args:
            file_path: Path to file

        Returns:
            Number of non-empty lines
        """
        line_count = 0

        try:
            # Try UTF-8 first
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # Strip whitespace
                    stripped = line.strip()

                    # Count non-empty lines (including comments)
                    if stripped:
                        line_count += 1

        except Exception as e:
            # Try with different encoding
            try:
                with open(file_path, 'r', encoding='latin-1', errors='ignore') as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped:
                            line_count += 1
            except:
                raise Exception(f"Could not read file with any encoding: {e}")

        return line_count

    def _calculate_grade(self, files_under_limit: int, total_files: int) -> float:
        """
        Calculate grade as percentage of files under line limit.

        Formula: (files_under_limit / total_files) * 100

        Args:
            files_under_limit: Number of files with < LINE_LIMIT lines
            total_files: Total number of code files

        Returns:
            Grade as float (0.00-100.00), rounded to 2 decimal places
        """
        if total_files == 0:
            return 0.00

        percentage = (files_under_limit / total_files) * 100
        return round(percentage, 2)
