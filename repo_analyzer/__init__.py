"""
Repository Analyzer Agent - Automated code grading tool for educational institutions.

Analyzes GitHub repositories to calculate code metrics and grades based on
file structure and line count distribution.
"""

from .analyzer import RepositoryAnalyzer
from .config import VERSION

__version__ = VERSION
__all__ = ['RepositoryAnalyzer']
