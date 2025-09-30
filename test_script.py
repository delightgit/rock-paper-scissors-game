import unittest
from unittest.mock import patch
from script import get_computer_choice, determine_winner, TIE, PLAYER_WIN, COMPUTER_WIN

class TestRockPaperScissors(unittest.TestCase):
    
    def test_get_computer_choice_returns_valid_choice(self):
        """Test that get_computer_choice returns a valid choice"""
        valid_choices = ['rock', 'paper', 'scissors']
        for _ in range(10):  # Test multiple times due to randomness
            choice = get_computer_choice()
            self.assertIn(choice, valid_choices)
    
    def test_determine_winner_tie_cases(self):
        """Test tie scenarios"""
        self.assertEqual(determine_winner('rock', 'rock'), TIE)
        self.assertEqual(determine_winner('paper', 'paper'), TIE)
        self.assertEqual(determine_winner('scissors', 'scissors'), TIE)
    
    def test_determine_winner_player_wins(self):
        """Test scenarios where player wins"""
        self.assertEqual(determine_winner('rock', 'scissors'), PLAYER_WIN)
        self.assertEqual(determine_winner('paper', 'rock'), PLAYER_WIN)
        self.assertEqual(determine_winner('scissors', 'paper'), PLAYER_WIN)
    
    def test_determine_winner_computer_wins(self):
        """Test scenarios where computer wins"""
        self.assertEqual(determine_winner('scissors', 'rock'), COMPUTER_WIN)
        self.assertEqual(determine_winner('rock', 'paper'), COMPUTER_WIN)
        self.assertEqual(determine_winner('paper', 'scissors'), COMPUTER_WIN)
    
    def test_determine_winner_invalid_inputs(self):
        """Test invalid inputs to ensure graceful handling"""
        # Invalid player choice with valid computer choice
        self.assertEqual(determine_winner('invalid', 'rock'), COMPUTER_WIN)
        self.assertEqual(determine_winner('spock', 'paper'), COMPUTER_WIN)
        self.assertEqual(determine_winner('', 'scissors'), COMPUTER_WIN)
        
        # Valid player choice with invalid computer choice
        self.assertEqual(determine_winner('rock', 'invalid'), COMPUTER_WIN)
        self.assertEqual(determine_winner('paper', 'lizard'), COMPUTER_WIN)
        
        # Both invalid
        self.assertEqual(determine_winner('invalid', 'also_invalid'), COMPUTER_WIN)
        
        # Case sensitivity (if applicable)
        self.assertEqual(determine_winner('ROCK', 'scissors'), COMPUTER_WIN)
        self.assertEqual(determine_winner('Paper', 'rock'), COMPUTER_WIN)
    
    @patch('random.choice')
    def test_get_computer_choice_mocked(self, mock_choice):
        """Test get_computer_choice with mocked random.choice"""
        mock_choice.return_value = 'paper'
        result = get_computer_choice()
        self.assertEqual(result, 'paper')
        mock_choice.assert_called_once_with(['rock', 'paper', 'scissors'])

if __name__ == '__main__':
    unittest.main()
