import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Define constants for result values
TIE = "tie"
PLAYER_WIN = "player_win"
COMPUTER_WIN = "computer_win"

def determine_winner(player, computer):
    if player == computer:
        return TIE
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return PLAYER_WIN
    else:
        return COMPUTER_WIN
    
def main():
    player_score = 0
    computer_score = 0
    input_map = {
        'rock': 'rock', 'r': 'rock',
        'paper': 'paper', 'p': 'paper',
        'scissors': 'scissors', 's': 'scissors'
    }
    
    while True:
        player_input = input("Enter rock (r), paper (p), scissors (s) or quit to exit: ").lower().strip()
        # The input is converted to lowercase above, so the check below is case-insensitive.
        if player_input == 'quit':
            print("Thanks for playing!")
            break
        if player_input not in input_map:
            print("Invalid choice. Please try again.")
            continue
        
        player = input_map[player_input]
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")
        
        result = determine_winner(player, computer)
        # Print a user-friendly message
        if result == PLAYER_WIN:
            print("You win!")
            player_score += 1
        elif result == COMPUTER_WIN:
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        print("-" * 20)

if __name__ == "__main__":
    main()
