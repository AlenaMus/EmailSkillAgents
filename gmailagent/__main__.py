"""
GmailAgent - Main module entry point

This allows gmailagent to be run as a module:
    python -m gmailagent auth
    python -m gmailagent export --label homework
"""

from .cli import cli

if __name__ == "__main__":
    cli()
