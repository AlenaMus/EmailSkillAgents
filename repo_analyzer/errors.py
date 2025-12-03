"""
Custom exceptions for Repository Analyzer Agent.
"""


class RepositoryAnalyzerError(Exception):
    """Base exception for all repository analyzer errors."""
    pass


class ExcelError(RepositoryAnalyzerError):
    """Raised when Excel file operations fail."""
    pass


class ExcelNotFoundError(ExcelError):
    """Raised when Excel file is not found."""
    pass


class ExcelInvalidFormatError(ExcelError):
    """Raised when Excel file has invalid format or missing columns."""
    pass


class RepositoryError(RepositoryAnalyzerError):
    """Base exception for repository-related errors."""
    pass


class RepositoryNotFoundError(RepositoryError):
    """Raised when repository is not found (404)."""
    pass


class RepositoryTimeoutError(RepositoryError):
    """Raised when repository clone times out."""
    pass


class RepositoryAccessDeniedError(RepositoryError):
    """Raised when repository access is forbidden (403)."""
    pass


class InvalidURLError(RepositoryError):
    """Raised when repository URL is invalid."""
    pass


class NetworkError(RepositoryError):
    """Raised when network connection fails."""
    pass


class NoCodeFilesError(RepositoryAnalyzerError):
    """Raised when repository has no code files."""
    pass


class MetricsCalculationError(RepositoryAnalyzerError):
    """Raised when metrics calculation fails."""
    pass
