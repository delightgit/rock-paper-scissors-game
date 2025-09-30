import unittest
from unittest.mock import patch
from script import get_computer_choice, determine_winner

class TestRockPaperScissors(unittest.TestCase):
    
    def test_get_computer_choice_returns_valid_choice(self):
        """Test that get_computer_choice returns a valid choice"""
        valid_choices = ['rock', 'paper', 'scissors']
        for _ in range(10):  # Test multiple times due to randomness
            choice = get_computer_choice()
            self.assertIn(choice, valid_choices)
    
    def test_determine_winner_tie_cases(self):
        """Test tie scenarios"""
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")
    
    def test_determine_winner_player_wins(self):
        """Test scenarios where player wins"""
        self.assertEqual(determine_winner('rock', 'scissors'), "You win!")
        self.assertEqual(determine_winner('paper', 'rock'), "You win!")
        self.assertEqual(determine_winner('scissors', 'paper'), "You win!")
    
    def test_determine_winner_computer_wins(self):
        """Test scenarios where computer wins"""
        self.assertEqual(determine_winner('scissors', 'rock'), "Computer wins!")
        self.assertEqual(determine_winner('rock', 'paper'), "Computer wins!")
        self.assertEqual(determine_winner('paper', 'scissors'), "Computer wins!")
    
    def test_determine_winner_invalid_inputs(self):
        """Test invalid inputs to ensure graceful handling"""
        # Invalid player choice with valid computer choice
        self.assertEqual(determine_winner('invalid', 'rock'), "Computer wins!")
        self.assertEqual(determine_winner('spock', 'paper'), "Computer wins!")
        self.assertEqual(determine_winner('', 'scissors'), "Computer wins!")
        
        # Valid player choice with invalid computer choice
        self.assertEqual(determine_winner('rock', 'invalid'), "Computer wins!")
        self.assertEqual(determine_winner('paper', 'lizard'), "Computer wins!")
        
        # Both invalid
        self.assertEqual(determine_winner('invalid', 'also_invalid'), "Computer wins!")
        
        # Case sensitivity (if applicable)
        self.assertEqual(determine_winner('ROCK', 'scissors'), "Computer wins!")
        self.assertEqual(determine_winner('Paper', 'rock'), "Computer wins!")
    
    @patch('random.choice')
    def test_get_computer_choice_mocked(self, mock_choice):
        """Test get_computer_choice with mocked random.choice"""
        mock_choice.return_value = 'paper'
        result = get_computer_choice()
        self.assertEqual(result, 'paper')
        mock_choice.assert_called_once_with(['rock', 'paper', 'scissors'])

if __name__ == '__main__':
    unittest.main()
