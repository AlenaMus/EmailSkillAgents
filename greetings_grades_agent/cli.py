"""
CLI Interface for Personalized Greetings Agent
"""

import click
import sys
from pathlib import Path
from .greetings_agent import GreetingsAgent


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """
    Personalized Greetings Agent

    Adds personalized, persona-based greetings to student homework grades.
    """
    pass


@cli.command()
@click.option(
    '--input', '-i',
    required=True,
    type=click.Path(exists=True),
    help='Input graded Excel file from Repository Analyzer'
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    help='Output Excel file path (optional, auto-generated if not provided)'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Enable verbose output'
)
def greet(input, output, verbose):
    """
    Generate personalized greetings for graded students

    Examples:

        # Basic usage
        python -m greetings_grades_agent.cli greet --input output/homework_emails_graded.xlsx

        # Custom output
        python -m greetings_grades_agent.cli greet -i graded.xlsx -o custom_greetings.xlsx

        # Verbose mode
        python -m greetings_grades_agent.cli greet -i graded.xlsx --verbose
    """
    try:
        agent = GreetingsAgent(verbose=verbose)
        result = agent.run(input_path=input, output_path=output)

        if result['success']:
            sys.exit(0)
        else:
            click.echo("\nFailed to generate greetings", err=True)
            sys.exit(1)

    except Exception as e:
        click.echo(f"\nError: {str(e)}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    cli()
