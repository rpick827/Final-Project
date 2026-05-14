"""
Main entry point for the NBA Game Simulator. 
Coordinates team selection, game simulation, and result reporting.
"""

from teams import TEAMS, choose_team
from players import get_best_player
from game_engine import simulate_game, display_results

def main():
    """
    Runs the primary game loop, allowing users to simulate multiple NBA games.
    """
    while True:
        print("\n=== NBA GAME SIMULATOR ===")
        
        # Selection logic - choose_team now handles validation internally
        team1 = choose_team("Pick home team: ")
        team2 = choose_team("Pick away team: ")

        # Core simulation logic
        score1, score2 = simulate_game(team1, team2, TEAMS)
        
        # Determine winner and fetch the top player for that team
        winner = team1 if score1 > score2 else team2
        best = get_best_player(winner)

        # Output results in the original requested format
        display_results(team1, team2, score1, score2, best)

        # Loop control
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()