"""
This module manages the team data and user selection logic for the NBA simulator.
"""

# Expanded data to address "missing code" feedback
TEAMS = {
    "Lakers": {"offense": 112, "defense": 108},
    "Celtics": {"offense": 118, "defense": 105},
    "Warriors": {"offense": 115, "defense": 110},
    "Bulls": {"offense": 105, "defense": 107},
    "Suns": {"offense": 114, "defense": 112},
}

def choose_team(prompt: str) -> str:
    """
    Prompts the user to select a team and validates the input.
    
    Args:
        prompt (str): The text shown to the user.
        
    Returns:
        str: The validated name of the selected team.
    """
    while True:
        print(f"\nAvailable Teams: {', '.join(TEAMS.keys())}")
        choice = input(prompt).strip()
        
        # Check if the team exists in our dictionary
        if choice in TEAMS:
            return choice
        
        print(f"Error: '{choice}' is not a valid team. Please check your spelling.")