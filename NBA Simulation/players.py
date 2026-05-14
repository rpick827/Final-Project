"""
This module handles player data and player-specific logic.
"""

PLAYERS = {
    "Lakers": [{"name": "LeBron James", "rating": 95}, {"name": "Anthony Davis", "rating": 90}],
    "Celtics": [{"name": "Jayson Tatum", "rating": 92}, {"name": "Jaylen Brown", "rating": 89}],
    "Warriors": [{"name": "Steph Curry", "rating": 96}, {"name": "Draymond Green", "rating": 83}],
    "Bulls": [{"name": "Zach LaVine", "rating": 85}],
    "Suns": [{"name": "Kevin Durant", "rating": 94}],
}

def get_best_player(team_name: str) -> dict:
    """
    Retrieves the player with the highest rating from a specific team.
    
    Args:
        team_name (str): The name of the team to search.
        
    Returns:
        dict: The player dictionary (name and rating).
    """
    players = PLAYERS.get(team_name, [])
    if not players:
        return {"name": "Unknown", "rating": 0}
        
    return max(players, key=lambda p: p["rating"])