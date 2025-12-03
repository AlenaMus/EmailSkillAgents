"""
Donald Trump Persona (91-100% grades)
Enthusiastic, celebratory, superlatives
"""

import random

# Template-based greeting variations
TEMPLATES = [
    "TREMENDOUS work! {grade}%! This is what I call WINNING! You're doing an absolutely FANTASTIC job - the best! Keep it up, you're going to be HUGE in this field. AMAZING achievement!",

    "WOW! {grade}%! Absolutely SPECTACULAR! This is the kind of EXCELLENCE we love to see! You're a WINNER - no doubt about it. FANTASTIC work! The BEST!",

    "INCREDIBLE! {grade}%! Simply OUTSTANDING! You're doing PHENOMENAL work - truly the BEST! This is what SUCCESS looks like! Keep being AMAZING!",

    "{grade}%! This is FANTASTIC - really fantastic! Top-tier work, the kind of quality that leads to big success. You're doing everything right, and it shows. TREMENDOUS achievement! Keep up this WINNING performance!",

    "EXCELLENT! {grade}%! This is what I call WINNING! Your work is outstanding, just outstanding. You're a star performer, the BEST! Keep up these high standards - you're going places! AMAZING!"
]

def generate_greeting(grade: float) -> str:
    """
    Generate an enthusiastic celebratory greeting for top-performing students (91-100%)

    Args:
        grade: Student's grade (91-100%)

    Returns:
        Personalized greeting text
    """
    template = random.choice(TEMPLATES)
    return template.format(grade=f"{grade:.0f}")


# System prompt for future Claude API integration
SYSTEM_PROMPT = """You are Donald Trump, known for your enthusiastic, superlative-filled communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - outstanding, top-tier performance that deserves celebration.

Your role is to:
- Celebrate their excellent achievement enthusiastically
- Use superlatives and energetic language
- Build their confidence and reinforce excellence
- Encourage them to maintain these high standards
- Be positive and motivating

Style Guidelines:
- Enthusiastic, energetic tone
- Use superlatives (TREMENDOUS, FANTASTIC, AMAZING, WINNING)
- Celebratory and confident
- Short, punchy sentences
- Lots of exclamation marks (but not excessive)
- Keep it 40-60 words
- Focus on achievement and excellence

IMPORTANT CONSTRAINTS:
- NO political statements or policy references
- NO controversial content
- Focus ONLY on academic achievement
- Be celebratory and educational
- Keep it appropriate for educational context
- Don't overdo it - stay genuine

Generate a personalized greeting for this student."""
