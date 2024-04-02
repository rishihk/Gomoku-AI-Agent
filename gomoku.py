# Author: Hrishikesha H Kyathsandra
# References: https://github.com/aimacode

import numpy as np
from game import Game

class Gomoku(Game):
    """Gomoku game class."""
    def __init__(self):
        """Initializes the Gomoku game."""
        super().__init__(board_size=15)
        self.moves_played = 0

    def display(self):
        """Displays the current state of the Gomoku game board."""
        color_reset = "\033[0m"
        black_piece = "\033[91mB" + color_reset
        white_piece = "\033[93mW" + color_reset
        empty_slot = "\033[37m.\033[0m"

        for board_row in self.board:
            row_display = ' '.join([black_piece if cell == 'B' else white_piece if cell == 'W' else empty_slot for cell in board_row])
            print(row_display)
        print()

    def terminal_test(self, current_player):
        """Checks if the game has reached a terminal state."""
        return self.check_winner(self.board, current_player, self.size)

    def draw_test(self):
        """Checks if the game has ended in a draw."""
        return np.all(self.board != '.')

    def to_move(self, position, player_mark):
        """Makes a move on the Gomoku game board."""
        if self.is_valid_move(self.board, position, player_mark, self.moves_played):
            self.board[position[0]][position[1]] = player_mark
            self.last_move = position
            if player_mark == 'B':
                self.moves_played += 1
            return True
        return False

    def switch(self, current_player):
        """Switches the current player."""
        return 'W' if current_player == 'B' else 'B'

    def is_empty_position(self, row, col):
        """Checks if a position on the board is empty."""
        return self.board[row][col] == '.'

    def has_neighboring_stone(self, row, col):
        """Checks if a position on the board has a neighboring stone."""
        for delta_row in range(-1, 2):
            for delta_col in range(-1, 2):
                neighbor_row, neighbor_col = row + delta_row, col + delta_col
                if 0 <= neighbor_row < self.size and 0 <= neighbor_col < self.size:
                    if self.board[neighbor_row][neighbor_col] != '.':
                        return True
        return False

    def get_empty_positions(self):
        """Returns a list of empty positions on the board."""
        return [(row, col) for row in range(self.size) for col in range(self.size) if self.is_empty_position(row, col)]

    def get_good_moves(self):
        """Returns a list of potential good moves."""
        potential_moves = [pos for pos in self.get_empty_positions() if self.has_neighboring_stone(*pos)]
        return potential_moves if potential_moves else self.get_empty_positions()

    def check_direction_for_win(self, game_board, start_row, start_col, dx, dy, current_player):
        """Checks if a direction has a winning sequence of stones."""
        for i in range(1, 5):
            next_row, next_col = start_row + dx*i, start_col + dy*i
            if not (0 <= next_row < 15 and 0 <= next_col < 15 and game_board[next_row][next_col] == current_player):
                return False
        return True

    def check_winner(self, game_board, current_player, board_size=15):
        """Checks if the current player has won the game."""
        win_directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row_index in range(board_size):
            for col_index in range(board_size):
                if game_board[row_index][col_index] == current_player:
                    for dx, dy in win_directions:
                        if self.check_direction_for_win(game_board, row_index, col_index, dx, dy, current_player):
                            return True
        return False

    def check_initial_moves(self, current_move, moves_played):
        """Checks if the initial moves are valid."""
        if moves_played == 0:
            return current_move == (7, 7)
        elif moves_played == 1:
            delta_row = abs(current_move[0] - 7)
            delta_col = abs(current_move[1] - 7)
            return delta_row >= 3 or delta_col >= 3
        return False

    def is_valid_move(self, game_board, current_move, current_player, moves_played):
        """Checks if a move is valid."""
        if current_player == 'B':
            if moves_played < 2 and not self.check_initial_moves(current_move, moves_played):
                return False
        if 0 <= current_move[0] < 15 and 0 <= current_move[1] < 15:
            return game_board[current_move[0]][current_move[1]] == '.'
        return False
