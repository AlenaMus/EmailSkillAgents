"""
Main Greetings Agent Orchestrator
"""

from pathlib import Path
from typing import Optional, Dict, Any
from .excel_manager import ExcelManager
from .greeting_generator import GreetingGenerator
from .persona_manager import get_persona_display_name
from .config import OUTPUT_DIR, DEFAULT_OUTPUT_FILENAME


class GreetingsAgent:
    """
    Main orchestrator for personalized greetings generation
    """

    def __init__(self, verbose: bool = False):
        """
        Initialize greetings agent

        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.excel_manager = ExcelManager()
        self.greeting_generator = GreetingGenerator()
        self.stats = {
            'total_students': 0,
            'greetings_generated': 0,
            'skipped': 0,
            'persona_counts': {
                'dudi_amsalem': 0,
                'benjamin_netanyahu': 0,
                'shahar_hasson': 0,
                'donald_trump': 0
            }
        }

    def run(self, input_path: str, output_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Run the greetings agent end-to-end

        Args:
            input_path: Path to graded Excel file
            output_path: Optional output path (auto-generated if not provided)

        Returns:
            Dictionary with execution results
        """
        self._print_header()

        # Determine output path
        if output_path is None:
            output_path = Path(OUTPUT_DIR) / DEFAULT_OUTPUT_FILENAME
        else:
            output_path = Path(output_path)

        # Validate input
        self._print(f"\nReading input: {input_path}")
        validation = self.excel_manager.validate_input_excel(input_path)

        if not validation['valid']:
            self._print("\nERROR: Invalid input Excel")
            for error in validation['errors']:
                self._print(f"  - {error}")
            return {'success': False, 'errors': validation['errors']}

        self._print(f"Found {validation['graded_count']} students with grades")
        if validation['error_count'] > 0:
            self._print(f"Found {validation['error_count']} students without grades (will skip)")

        # Read Excel
        wb, students = self.excel_manager.read_graded_excel(input_path)
        self.stats['total_students'] = len(students)

        # Generate greetings
        self._print("\nGenerating personalized greetings...\n")
        greetings = []

        for idx, student in enumerate(students, start=1):
            grade = student.get('Grade')
            greeting, persona = self.greeting_generator.generate(grade)
            greetings.append((greeting, persona))

            # Update stats
            if greeting != "N/A":
                self.stats['greetings_generated'] += 1
                if persona:
                    self.stats['persona_counts'][persona] = \
                        self.stats['persona_counts'].get(persona, 0) + 1
            else:
                self.stats['skipped'] += 1

            # Print progress
            persona_display = get_persona_display_name(persona) if persona else "N/A (No grade available)"
            grade_display = f"{grade:.0f}%" if grade is not None else "N/A"
            self._print(f"[{idx}/{len(students)}] Grade: {grade_display:6} -> Persona: {persona_display}")

        # Write output Excel
        self._print(f"\nWriting output to: {output_path}")
        self.excel_manager.write_with_greetings(wb, students, greetings, str(output_path))

        # Print summary
        self._print_summary(output_path)

        return {
            'success': True,
            'output_path': str(output_path),
            'stats': self.stats
        }

    def _print_header(self):
        """Print agent header"""
        self._print("=" * 50)
        self._print("Personalized Greetings Agent v1.0")
        self._print("=" * 50)

    def _print_summary(self, output_path: Path):
        """Print execution summary"""
        self._print("\n" + "=" * 50)
        self._print("Summary")
        self._print("=" * 50)
        self._print(f"Total Students: {self.stats['total_students']}")
        self._print(f"Greetings Generated: {self.stats['greetings_generated']}")
        self._print(f"Skipped (no grade): {self.stats['skipped']}")

        self._print("\nPersonas Used:")
        self._print(f"  - Dudi Amsalem (0-50%): {self.stats['persona_counts']['dudi_amsalem']}")
        self._print(f"  - Netanyahu (51-70%): {self.stats['persona_counts']['benjamin_netanyahu']}")
        self._print(f"  - Shahar Hasson (71-90%): {self.stats['persona_counts']['shahar_hasson']}")
        self._print(f"  - Donald Trump (91-100%): {self.stats['persona_counts']['donald_trump']}")

        self._print(f"\nOutput: {output_path}")
        self._print("\n[OK] Greetings complete!")

    def _print(self, message: str):
        """Print message (respects verbose setting)"""
        print(message)
