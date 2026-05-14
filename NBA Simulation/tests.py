import unittest
from game_engine import simulate_game
from players import get_best_player

class TestNBASimulator(unittest.TestCase):
    
    def setUp(self):
        self.mock_teams = {
            "TeamA": {"offense": 100, "defense": 100},
            "TeamB": {"offense": 100, "defense": 100}
        }

    def test_score_generation(self):
        """Test that scores are returned as integers."""
        s1, s2 = simulate_game("TeamA", "TeamB", self.mock_teams)
        self.assertIsInstance(s1, int)
        self.assertIsInstance(s2, int)

    def test_best_player_logic(self):
        """Test that the highest rated player is correctly identified."""
        best = get_best_player("Lakers")
        self.assertEqual(best["name"], "LeBron James")

if __name__ == "__main__":
    unittest.main()