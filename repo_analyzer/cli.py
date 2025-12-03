"""
Command-line interface for Repository Analyzer Agent.
"""

import sys
import click
from pathlib import Path

from .analyzer import RepositoryAnalyzer
from .config import VERSION
from .errors import ExcelError, RepositoryAnalyzerError


@click.group()
@click.version_option(version=VERSION, prog_name='Repository Analyzer')
def cli():
    """
    Repository Analyzer Agent - Automated code grading tool.

    Analyzes GitHub repositories to calculate code metrics and grades
    based on file structure and line count distribution.
    """
    pass


@cli.command()
@click.option(
    '--input',
    '-i',
    'input_path',
    required=True,
    type=click.Path(exists=True, dir_okay=False, readable=True),
    help='Path to input Excel file from GmailAgent'
)
@click.option(
    '--output',
    '-o',
    'output_path',
    type=click.Path(dir_okay=False, writable=True),
    help='Path to output Excel file (optional, auto-generated if not specified)'
)
@click.option(
    '--verbose',
    '-v',
    is_flag=True,
    help='Enable verbose output'
)
def analyze(input_path: str, output_path: str, verbose: bool):
    """
    Analyze repositories from Excel file and generate graded output.

    Reads an Excel file containing repository URLs, clones each repository,
    calculates code metrics (lines, files, grade), and outputs an enhanced
    Excel file with grades and summary statistics.

    Example:

        python -m repo_analyzer.cli analyze --input homework_emails.xlsx

        python -m repo_analyzer.cli analyze -i hw.xlsx -o graded.xlsx
    """
    try:
        # Validate input file
        input_path = Path(input_path)
        if not input_path.exists():
            click.echo(click.style(f"Error: Input file not found: {input_path}", fg='red'))
            sys.exit(1)

        # Validate output path if provided
        if output_path:
            output_path = Path(output_path)
            if not output_path.parent.exists():
                click.echo(
                    click.style(
                        f"Error: Output directory does not exist: {output_path.parent}",
                        fg='red'
                    )
                )
                sys.exit(1)

        # Create analyzer
        analyzer = RepositoryAnalyzer(verbose=verbose)

        # Run analysis
        try:
            summary = analyzer.analyze(
                input_path=str(input_path),
                output_path=str(output_path) if output_path else None
            )

            # Success
            sys.exit(0)

        except ExcelError as e:
            click.echo(click.style(f"Excel Error: {str(e)}", fg='red'))
            sys.exit(1)

        except RepositoryAnalyzerError as e:
            click.echo(click.style(f"Analysis Error: {str(e)}", fg='red'))
            sys.exit(1)

        except KeyboardInterrupt:
            click.echo()
            click.echo(click.style("Analysis interrupted by user.", fg='yellow'))
            sys.exit(130)

        except Exception as e:
            click.echo(click.style(f"Unexpected Error: {str(e)}", fg='red'))
            if verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)

    except Exception as e:
        click.echo(click.style(f"Fatal Error: {str(e)}", fg='red'))
        sys.exit(1)


@cli.command()
def version():
    """Display version information."""
    click.echo(f"Repository Analyzer v{VERSION}")


if __name__ == '__main__':
    cli()
