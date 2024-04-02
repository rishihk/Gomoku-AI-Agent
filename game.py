# Author: Hrishikesha H Kyathsandra
# References: https://github.com/aimacode

import numpy as np

class Game:
    """Game class."""
    def __init__(self, board_size=15):
        """Initializes the game."""
        self.size = board_size
        self.board = np.full((self.size, self.size), '.', dtype=str)
        self.player = 'B'
        self.last_move = None

    def to_move(self, move, player):
        """Makes a move on the game board."""
        pass

    def terminal_test(self, player):
        """Checks if the game has reached a terminal state."""
        pass

    def draw_test(self):
        """Checks if the game has ended in a draw."""
        pass

    def switch_(self, player):
        """Switches the current player."""
        pass

    def display(self):
        """Displays the current state of the game board."""
        for row in self.board:
            print(' '.join(row))
        print()