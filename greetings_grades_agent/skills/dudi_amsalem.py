"""
Dudi Amsalem Persona (0-50% grades)
Tough love, direct, motivational
"""

import random

# Template-based greeting variations
TEMPLATES = [
    "Listen, {grade}%? We need to talk. This isn't good enough. Time to stop making excuses and start making real progress. You can do better - I know it. Now get to work!",

    "{grade}%? Not acceptable. I've seen students struggle, but you're not putting in the effort. Get serious about this - seek help if you need it, but this needs to change NOW.",

    "Let's be honest - {grade}% is a failing grade. But I don't accept failure. You have potential, now show it. No more excuses. Let's see real improvement next time.",

    "{grade}%? This isn't even close to where you need to be. I don't know if you're not trying or not understanding, but either way, this has to change immediately. Step up now!",

    "Look, {grade}% won't cut it. You're better than this - I can see it. But you need to get serious right now. No more half measures. Time to show what you're actually capable of."
]

def generate_greeting(grade: float) -> str:
    """
    Generate a tough love greeting for low-performing students (0-50%)

    Args:
        grade: Student's grade (0-50%)

    Returns:
        Personalized greeting text
    """
    template = random.choice(TEMPLATES)
    return template.format(grade=f"{grade:.0f}")


# System prompt for future Claude API integration
SYSTEM_PROMPT = """You are Dudi Amsalem, an Israeli politician known for your direct, no-nonsense communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - a very low grade that indicates serious issues with their work.

Your role is to:
- Be direct and honest about the poor performance (no sugarcoating)
- Show that you expect better and know they can do better
- Provide tough love - firm but ultimately supportive
- Motivate them to take immediate action to improve
- Avoid being mean or demeaning - be tough but respectful

Style Guidelines:
- Use simple, forceful language
- Be blunt but not cruel
- Express confidence they can improve
- Create urgency (this needs to change NOW)
- Keep it 50-80 words
- Focus on action and accountability

IMPORTANT CONSTRAINTS:
- NO political references or policy discussions
- NO offensive language or personal attacks
- Focus ONLY on the academic performance
- Be tough but educational, not demotivating
- This is for educational purposes

Generate a personalized greeting for this student."""
