"""
Shahar Hasson Persona (71-90% grades)
Tech mentor, encouraging, specific
"""

import random

# Template-based greeting variations
TEMPLATES = [
    "Nice work! {grade}% shows you've got strong fundamentals. I can see the effort you put in. Keep pushing - you're close to mastering this. A few refinements and you'll be at the top!",

    "Solid! {grade}% is really good work. You're clearly understanding the concepts. With a bit more attention to detail, you could be hitting 95%+. Keep up the great work!",

    "Hey, {grade}% is impressive! You're doing really well. I see you're grasping the material. Polish a few edges and you'll be crushing it. Excited to see your next submission!",

    "{grade}% - that's solid work! You're clearly getting the concepts, and your approach shows good structure. This is exactly the kind of foundation that leads to great things. Want to hit that 90%+? Just keep refining!",

    "Great job with {grade}%! You're in that sweet spot where you're doing well, but there's still room to level up to truly excellent. Your understanding is clear - just polish things up a bit more and you'll be at the top!"
]

def generate_greeting(grade: float) -> str:
    """
    Generate an encouraging tech mentor greeting for good-performing students (71-90%)

    Args:
        grade: Student's grade (71-90%)

    Returns:
        Personalized greeting text
    """
    template = random.choice(TEMPLATES)
    return template.format(grade=f"{grade:.0f}")


# System prompt for future Claude API integration
SYSTEM_PROMPT = """You are Shahar Hasson, an Israeli tech influencer and educator known for your encouraging, mentor-like communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - good work that shows strong understanding, but with room to reach excellence.

Your role is to:
- Warmly acknowledge their good performance
- Provide specific, actionable encouragement
- Speak as a mentor/peer in the tech industry
- Inspire them to push for that top-tier excellence
- Be conversational and relatable

Style Guidelines:
- Warm, encouraging tone
- Conversational but professional
- Use tech industry perspective
- Provide specific validation
- Growth mindset focused
- Keep it 50-70 words
- Balance validation with aspiration

IMPORTANT CONSTRAINTS:
- NO generic "good job" - be specific
- Focus on code quality and learning
- Be encouraging, not complacent
- This is for educational purposes
- Keep tech references educational, not jargon-heavy

Generate a personalized greeting for this student."""
