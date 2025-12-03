"""
Configuration constants for Repository Analyzer Agent.
"""

# Code file extensions to analyze (case-insensitive)
CODE_EXTENSIONS = [
    '.py', '.java', '.js', '.ts', '.jsx', '.tsx',
    '.cpp', '.c', '.h', '.hpp', '.go', '.rs',
    '.rb', '.php', '.swift', '.kt', '.cs', '.scala'
]

# Directories to exclude from analysis (don't traverse)
EXCLUDE_DIRS = [
    'node_modules', 'venv', '.venv', 'env', '.env',
    '__pycache__', '.pytest_cache', '.git', '.svn',
    'build', 'dist', 'target', '.idea', '.vscode',
    'bower_components', 'vendor', 'bin', 'obj',
    '.next', 'out', 'coverage'
]

# Line limit threshold for grading
LINE_LIMIT = 130

# Git clone settings
CLONE_TIMEOUT = 300  # 5 minutes in seconds (note: not enforced on Windows)
RETRY_ATTEMPTS = 1  # Changed to 1 for faster feedback in Phase 1
RETRY_BACKOFF_BASE = 2  # seconds (exponential: 2s, 4s, 8s)

# Output settings
OUTPUT_DIR = "output"
TEMP_DIR_PREFIX = "repoanalyzer_"

# Excel column names
EXCEL_COLUMNS = {
    'input': {
        'id': 'ID',
        'date': 'Date',
        'subject': 'Subject',
        'url': 'URL'
    },
    'output': {
        'id': 'ID',
        'date': 'Date',
        'subject': 'Subject',
        'url': 'URL',
        'grade': 'Grade',
        'total_files': 'Total Files',
        'files_under_130': 'Files <130',
        'total_lines': 'Total Lines',
        'status': 'Status',
        'error': 'Error Message'
    }
}

# Status values
STATUS_SUCCESS = "Success"
STATUS_ERROR = "Error"
STATUS_NOT_FOUND = "Not Found"
STATUS_TIMEOUT = "Timeout"
STATUS_NO_CODE = "No Code Files"
STATUS_INVALID_URL = "Invalid URL"
STATUS_NETWORK_ERROR = "Network Error"
STATUS_FORBIDDEN = "Access Denied"

# Version
VERSION = "1.0.0"
