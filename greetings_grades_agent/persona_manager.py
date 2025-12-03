"""
Persona Manager - Determines which persona to use based on grade
"""

from typing import Optional
from .config import GRADE_RANGES, PERSONA_NAMES


def determine_persona(grade: Optional[float]) -> Optional[str]:
    """
    Determine which persona to use based on grade

    Args:
        grade: Student's grade (0-100) or None

    Returns:
        Persona identifier string or None if no grade

    Examples:
        >>> determine_persona(45.0)
        'dudi_amsalem'
        >>> determine_persona(65.0)
        'benjamin_netanyahu'
        >>> determine_persona(85.0)
        'shahar_hasson'
        >>> determine_persona(95.0)
        'donald_trump'
        >>> determine_persona(None)
        None
    """
    if grade is None:
        return None

    # Dudi Amsalem: 0-50% (inclusive)
    if 0 <= grade <= 50:
        return 'dudi_amsalem'

    # Benjamin Netanyahu: 51-70% (inclusive)
    elif 50 < grade <= 70:
        return 'benjamin_netanyahu'

    # Shahar Hasson: 71-90% (inclusive)
    elif 70 < grade <= 90:
        return 'shahar_hasson'

    # Donald Trump: 91-100% (inclusive)
    elif 90 < grade <= 100:
        return 'donald_trump'

    # Out of range (shouldn't happen)
    else:
        return None


def get_persona_display_name(persona: str) -> str:
    """
    Get display name for a persona

    Args:
        persona: Persona identifier

    Returns:
        Display name for the persona
    """
    return PERSONA_NAMES.get(persona, 'N/A')
