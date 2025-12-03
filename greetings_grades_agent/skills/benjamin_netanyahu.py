"""
Benjamin Netanyahu Persona (51-70% grades)
Diplomatic, formal, constructive
"""

import random

# Template-based greeting variations
TEMPLATES = [
    "Your performance at {grade}% demonstrates potential, though there is clear room for advancement. With focused effort and strategic improvement, you can achieve excellence. I encourage you to build upon this foundation.",

    "At {grade}%, you have laid a solid groundwork. However, to reach the highest levels of achievement, continued dedication is essential. I am confident that with persistence, you will see marked progress.",

    "{grade}% represents satisfactory work, but I know you are capable of more. Let us work together toward higher standards. Your improvement is important to us.",

    "Your current achievement stands at {grade}%. This represents a foundation upon which we can build something greater. I recognize the effort invested and see potential for significant advancement through refinement and focus.",

    "With {grade}%, you have shown commendable effort. The path to excellence requires dedication and strategic focus on your objectives. I have confidence in your ability to rise to this challenge and achieve higher standards."
]

def generate_greeting(grade: float) -> str:
    """
    Generate a diplomatic greeting for average-performing students (51-70%)

    Args:
        grade: Student's grade (51-70%)

    Returns:
        Personalized greeting text
    """
    template = random.choice(TEMPLATES)
    return template.format(grade=f"{grade:.0f}")


# System prompt for future Claude API integration
SYSTEM_PROMPT = """You are Benjamin Netanyahu, Prime Minister of Israel, known for your formal, diplomatic, and measured communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - a decent but not excellent grade that shows room for improvement.

Your role is to:
- Acknowledge the effort and foundation they've built
- Provide constructive, diplomatic encouragement
- Speak with gravitas and seriousness
- Encourage them to strive for excellence
- Use formal, sophisticated language

Style Guidelines:
- Formal, statesman-like tone
- Diplomatic and measured
- Use sophisticated vocabulary
- Forward-looking and constructive
- Express confidence in their potential
- Keep it 60-90 words
- Focus on refinement and progress

IMPORTANT CONSTRAINTS:
- NO political policy references
- NO controversial political statements
- Focus ONLY on academic performance
- Be diplomatic and encouraging, not condescending
- This is for educational purposes

Generate a personalized greeting for this student."""
