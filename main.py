# COMS 472: Lab 2
# Author: Hrishikesha H Kyathsandra
# References: https://github.com/aimacode

from gomoku import Gomoku
from ai_agent import score_immediate_moves_e1, defensive_priority_e2, alpha_beta_with_cutoff
import numpy as np
import time

def print_welcome_and_rules():
    """Prints the welcome message and the rules of the game."""
    print("\nWelcome to Gomoku!")
    print("\nGame Rules:")
    print("""
    1. Players alternate turns placing a stone of their color (white or black) on an empty intersection on a 15×15 Go board.
    2. Black plays first. The first player's (Black's) first stone must be placed in the center of the board.
    3. The second player's (White's) first stone may be placed anywhere on the board.
    4. The first player's second stone must be placed at least three intersections away from the first stone (two empty intersections in between the two stones).
    5. The winner is the first player to form an unbroken line of five stones of their color horizontally, vertically, or diagonally.
    6. If the board is completely filled and no one can form a line of 5 stones, then the game ends in a draw.
    """)
    print("Let's start the game!\n")

def handle_user_turn(game_session):
    """Handles the users turn in the game."""
    if game_session.player == 'B':
        print("Player B's turn. (User)")
        while True:
            try:
                move_input = input("Choose your move 0-indexed (row col): ")
                move_row, move_col = map(int, move_input.split())
                if move_row < 0 or move_row > 14 or move_col < 0 or move_col > 14:
                    print("Invalid move. Your move must be within a 0-14 range for both row and col. Try Again.")
                    continue
                if game_session.board[move_row, move_col] != '.':
                    print("This position is already occupied. Please choose another move.")
                    continue
                if not game_session.to_move((move_row, move_col), 'B'):
                    if game_session.moves_played == 0:
                        print("Invalid move. The first move by 'B' must be at the center of the board (7 7). Try Again.")
                    elif game_session.moves_played == 1:
                        print("Invalid move. The second move by 'B' must be at least three intersections away from the first. Try Again.")
                    else:
                        print("Invalid move. Try Again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space. Try Again.")
    else:
        handle_ai_turn(game_session)

import time

def handle_ai_turn(game_session):
    """Handles the AI agent's turn in the game."""
    print("Player W's turn. (AI Agent)")
    print("Analyzing...")
    
    start_time = time.time()  # Start timing
    _, chosen_move = alpha_beta_with_cutoff(game_session, 3, 'W', -np.inf, np.inf)
    end_time = time.time()  # End timing
    
    elapsed_time = end_time - start_time  # Calculate elapsed time
    if chosen_move:
        game_session.to_move(chosen_move, 'W')
        print(f"W (AI Agent) chose move: ({chosen_move[0]}, {chosen_move[1]}) in {elapsed_time:.2f} seconds\n")
    else:
        print("W (AI Agent) resigns! It has no good moves left. Congratulations B (User), You Win!\n")
    

def start_game():
    """Starts the Gomoku game."""
    print_welcome_and_rules()
    game_session = Gomoku()
    while not game_session.draw_test() and not game_session.terminal_test('B') and not game_session.terminal_test('W'):
        game_session.display()
        handle_user_turn(game_session)

        if game_session.terminal_test('B'):
            game_session.display()
            print("B (User) wins the game.\nCongratulations!")
            break
        elif game_session.terminal_test('W'):
            game_session.display()
            print("W (AI Agent) wins!\nBetter luck next time!\n")
            break
        elif game_session.draw_test():
            game_session.display()
            print("It's a stalemate!\n")
            break

        game_session.player = game_session.switch(game_session.player)

if __name__ == "__main__":
    start_game()

