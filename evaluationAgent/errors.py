"""
Custom exceptions for Evaluation Gmail Sender Agent.

This module defines all custom exception classes used throughout the agent
for better error handling and reporting.
"""


class EvaluationAgentError(Exception):
    """Base exception for all evaluation agent errors."""
    pass


class ExcelError(EvaluationAgentError):
    """Base exception for Excel-related errors."""
    pass


class ExcelFileNotFoundError(ExcelError):
    """Raised when the Excel file is not found."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        super().__init__(f"Excel file not found: {filepath}")


class ExcelReadError(ExcelError):
    """Raised when there's an error reading the Excel file."""

    def __init__(self, filepath: str, reason: str):
        self.filepath = filepath
        self.reason = reason
        super().__init__(f"Error reading Excel file '{filepath}': {reason}")


class ExcelValidationError(ExcelError):
    """Raised when Excel file structure is invalid."""

    def __init__(self, message: str, missing_columns: list = None):
        self.missing_columns = missing_columns or []
        super().__init__(message)


class GmailError(EvaluationAgentError):
    """Base exception for Gmail API errors."""
    pass


class GmailAuthenticationError(GmailError):
    """Raised when Gmail authentication fails."""

    def __init__(self, message: str = "Gmail authentication failed"):
        super().__init__(message)


class GmailAPIError(GmailError):
    """Raised when Gmail API call fails."""

    def __init__(self, operation: str, reason: str):
        self.operation = operation
        self.reason = reason
        super().__init__(f"Gmail API error during '{operation}': {reason}")


class GmailLabelError(GmailError):
    """Raised when there's an error with Gmail labels."""

    def __init__(self, label_name: str, reason: str):
        self.label_name = label_name
        self.reason = reason
        super().__init__(f"Error with label '{label_name}': {reason}")


class EmailGenerationError(EvaluationAgentError):
    """Raised when email generation fails."""

    def __init__(self, student_id: str, reason: str):
        self.student_id = student_id
        self.reason = reason
        super().__init__(f"Failed to generate email for student '{student_id}': {reason}")


class FileSystemError(EvaluationAgentError):
    """Raised when there's a file system error."""

    def __init__(self, operation: str, filepath: str, reason: str):
        self.operation = operation
        self.filepath = filepath
        self.reason = reason
        super().__init__(f"File system error during '{operation}' on '{filepath}': {reason}")


class ConfigurationError(EvaluationAgentError):
    """Raised when there's a configuration error."""

    def __init__(self, setting: str, reason: str):
        self.setting = setting
        self.reason = reason
        super().__init__(f"Configuration error for '{setting}': {reason}")


class ValidationError(EvaluationAgentError):
    """Raised when input validation fails."""

    def __init__(self, field: str, value: any, reason: str):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"Validation error for '{field}' (value: {value}): {reason}")
