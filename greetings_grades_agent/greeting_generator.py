"""
Greeting Generator - Generates personalized greetings using persona templates
"""

from typing import Optional
from .persona_manager import determine_persona
from .skills import dudi_amsalem, benjamin_netanyahu, shahar_hasson, donald_trump


class GreetingGenerator:
    """
    Generates personalized greetings based on student grades
    Uses template-based approach for MVP (can be upgraded to Claude API in future)
    """

    def __init__(self):
        """Initialize greeting generator"""
        self.persona_modules = {
            'dudi_amsalem': dudi_amsalem,
            'benjamin_netanyahu': benjamin_netanyahu,
            'shahar_hasson': shahar_hasson,
            'donald_trump': donald_trump
        }

    def generate(self, grade: Optional[float]) -> tuple[str, Optional[str]]:
        """
        Generate personalized greeting for a student based on their grade

        Args:
            grade: Student's grade (0-100) or None

        Returns:
            Tuple of (greeting_text, persona_name)
            Returns ("N/A", None) if no grade available

        Examples:
            >>> gen = GreetingGenerator()
            >>> greeting, persona = gen.generate(45.0)
            >>> persona
            'dudi_amsalem'
            >>> greeting, persona = gen.generate(None)
            >>> greeting
            'N/A'
        """
        # Handle missing grade
        if grade is None or grade == '':
            return "N/A", None

        # Convert to float if string
        if isinstance(grade, str):
            try:
                grade = float(grade)
            except ValueError:
                return "N/A", None

        # Determine persona based on grade
        persona = determine_persona(grade)

        if persona is None:
            return "N/A", None

        # Get the appropriate persona module
        persona_module = self.persona_modules.get(persona)

        if persona_module is None:
            return "N/A", None

        # Generate greeting using persona's template function
        try:
            greeting = persona_module.generate_greeting(grade)
            return greeting, persona
        except Exception as e:
            # Fallback in case of any error
            return f"Great work on your assignment! Keep it up!", persona

    def validate_greeting(self, greeting: str) -> bool:
        """
        Validate that a greeting is appropriate

        Args:
            greeting: Greeting text to validate

        Returns:
            True if appropriate, False otherwise
        """
        if not greeting or greeting == "N/A":
            return True

        # Check length (should be reasonable)
        word_count = len(greeting.split())
        if word_count < 5 or word_count > 200:
            return False

        # Check for minimum content
        if len(greeting.strip()) < 20:
            return False

        return True
