"""
This module implements a graphical Rock Paper Scissors game using Tkinter.
    RockPaperScissorsGUI: Manages the GUI, user interactions, and game logic.
Features:
    - Emoji-enhanced buttons for player choices (rock, paper, scissors).
    - Score tracking for both player and computer.
    - Visual feedback for each round's outcome.
    - Reset and quit controls.
    - Responsive, user-friendly interface.
This module implements a graphical version of the classic Rock Paper Scissors game using the Tkinter library for Python. 
It features a user-friendly interface with emoji-enhanced buttons, score tracking for both the player and the computer, 
and visual feedback for each round's outcome. The game allows users to reset scores and quit the application via control buttons.
Classes:
    RockPaperScissorsGUI: Handles the GUI layout, game logic, and user interactions.
Functions:
    main(): Initializes and runs the Tkinter application window.
Usage:
    Run this script directly to launch the Rock Paper Scissors GUI game.
Rock Paper Scissors GUI Game using Tkinter
A graphical version of the classic game with score tracking.
"""

import tkinter as tk
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x600")
        self.root.configure(bg='#2c3e50')
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']
        
        # Emojis for visual appeal
        self.choice_emojis = {
            'rock': '🪨',
            'paper': '📄', 
            'scissors': '✂️'
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🎮 Rock Paper Scissors 🎮",
            font=('Arial', 24, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=20)
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg='#2c3e50')
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            self.score_frame,
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}",
            font=('Arial', 16, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            padx=20,
            pady=10,
            relief='raised',
            bd=2
        )
        self.score_label.pack()
        
        # Choice buttons frame
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(pady=30)
        
        # Create choice buttons
        button_style = {
            'font': ('Arial', 14, 'bold'),
            'width': 12,
            'height': 3,
            'relief': 'raised',
            'bd': 3
        }
        
        self.rock_btn = tk.Button(
            buttons_frame,
            text="🪨 ROCK",
            command=lambda: self.play_game('rock'),
            bg='#95a5a6',
            fg='#2c3e50',
            activebackground='#bdc3c7',
            **button_style
        )
        self.rock_btn.grid(row=0, column=0, padx=10, pady=5)
        
        self.paper_btn = tk.Button(
            buttons_frame,
            text="📄 PAPER",
            command=lambda: self.play_game('paper'),
            bg='#3498db',
            fg='black',
            activebackground='#5dade2',
            **button_style
        )
        self.paper_btn.grid(row=0, column=1, padx=10, pady=5)
        
        self.scissors_btn = tk.Button(
            buttons_frame,
            text="✂️ SCISSORS",
            command=lambda: self.play_game('scissors'),
            bg="#911339",
            fg='black',
            activebackground='#ec7063',
            **button_style
        )
        self.scissors_btn.grid(row=0, column=2, padx=10, pady=5)
        
        # Game result display
        self.result_frame = tk.Frame(self.root, bg='#2c3e50')
        self.result_frame.pack(pady=30)
        
        # Choices display
        self.choices_label = tk.Label(
            self.result_frame,
            text="Make your choice!",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.choices_label.pack(pady=5)
        
        self.vs_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='#f39c12'
        )
        self.vs_label.pack(pady=10)
        
        # Result message
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='#e74c3c',
            wraplength=400
        )
        self.result_label.pack(pady=10)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg='#2c3e50')
        control_frame.pack(pady=20)
        
        self.reset_btn = tk.Button(
            control_frame,
            text="🔄 Reset Score",
            command=self.reset_game,
            font=('Arial', 12, 'bold'),
            bg='#f39c12',
            fg='white',
            activebackground='#f4d03f',
            padx=20,
            pady=5,
            relief='raised',
            bd=2
        )
        self.reset_btn.pack(side=tk.LEFT, padx=10)
        
        self.quit_btn = tk.Button(
            control_frame,
            text="❌ Quit Game",
            command=self.root.quit,
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            activebackground='#ec7063',
            padx=20,
            pady=5,
            relief='raised',
            bd=2
        )
        self.quit_btn.pack(side=tk.LEFT, padx=10)
    
    def get_computer_choice(self):
        """Get random computer choice"""
        return random.choice(self.choices)
    
    def determine_winner(self, player, computer):
        """Determine the winner of the round"""
        if player == computer:
            return "It's a tie! 🤝"
        elif ((player == 'rock' and computer == 'scissors') or
              (player == 'paper' and computer == 'rock') or
              (player == 'scissors' and computer == 'paper')):
            return "You win! 🎉"
        else:
            return "Computer wins! 🤖"
    
    def play_game(self, player_choice):
        """Main game logic when player makes a choice"""
        computer_choice = self.get_computer_choice()
        
        # Display choices
        player_emoji = self.choice_emojis[player_choice]
        computer_emoji = self.choice_emojis[computer_choice]
        
        self.choices_label.config(text=f"You chose: {player_choice.title()}")
        self.vs_label.config(text=f"{player_emoji} VS {computer_emoji}")
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores
        if "You win" in result:
            self.player_score += 1
            self.result_label.config(fg='#27ae60')  # Green for win
        elif "Computer wins" in result:
            self.computer_score += 1
            self.result_label.config(fg='#e74c3c')  # Red for loss
        else:
            self.result_label.config(fg='#f39c12')  # Orange for tie
        
        # Update display
        self.result_label.config(text=result)
        self.update_score_display()
        
        # Add computer choice info
        computer_text = f"Computer chose: {computer_choice.title()}"
        self.choices_label.config(text=f"You: {player_choice.title()} | Computer: {computer_choice.title()}")
    
    def update_score_display(self):
        """Update the score display"""
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Computer: {self.computer_score}"
        )
    
    def reset_game(self):
        """Reset the game scores and display"""
        self.player_score = 0
        self.computer_score = 0
        self.update_score_display()
        
        # Clear result displays
        self.choices_label.config(text="Make your choice!")
        self.vs_label.config(text="")
        self.result_label.config(text="Game Reset! Good luck! 🍀", fg='#3498db')

def main():
    """Run the GUI application"""
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()