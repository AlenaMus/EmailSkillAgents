"""
Configuration constants for Personalized Greetings Agent
"""

# Grade range thresholds for persona selection
GRADE_RANGES = {
    'dudi_amsalem': (0, 50),      # Tough love (0-50%)
    'benjamin_netanyahu': (51, 70),  # Diplomatic (51-70%)
    'shahar_hasson': (71, 90),    # Tech mentor (71-90%)
    'donald_trump': (91, 100)     # Celebratory (91-100%)
}

# Output directory
OUTPUT_DIR = "greetings_results"

# Default output filename
DEFAULT_OUTPUT_FILENAME = "homework_emails_with_greetings.xlsx"

# Excel column configuration
EXCEL_COLUMNS = [
    'ID', 'Date', 'Subject', 'URL', 'Grade',
    'Total Files', 'Files <130', 'Total Lines',
    'Status', 'Error Message'
]

# New columns to add
NEW_COLUMNS = ['Personalized Greeting', 'Greeting Persona']

# Persona display names
PERSONA_NAMES = {
    'dudi_amsalem': 'Dudi Amsalem',
    'benjamin_netanyahu': 'Benjamin Netanyahu',
    'shahar_hasson': 'Shahar Hasson',
    'donald_trump': 'Donald Trump'
}
