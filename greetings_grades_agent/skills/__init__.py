"""
Persona Skills Package

Contains greeting templates and system prompts for each persona:
- dudi_amsalem: Tough love (0-50%)
- benjamin_netanyahu: Diplomatic (51-70%)
- shahar_hasson: Tech mentor (71-90%)
- donald_trump: Celebratory (91-100%)
"""

from . import dudi_amsalem
from . import benjamin_netanyahu
from . import shahar_hasson
from . import donald_trump

__all__ = [
    'dudi_amsalem',
    'benjamin_netanyahu',
    'shahar_hasson',
    'donald_trump'
]
