
# Author: Hrishikesha H Kyathsandra
# References: https://github.com/aimacode

import numpy as np
from gomoku import Gomoku

def score_immediate_moves_e1(current_game, current_player):
    """Returns the score of the current game state based on the immediate moves evaluation function."""
    potential_score = 0
    immediate_win = 10000
    immediate_block = -5000
    
    if current_game.terminal_test(current_player):
        return np.inf if current_player == 'W' else -np.inf
    opponent_player = current_game.switch(current_player)
    if current_game.terminal_test(opponent_player):
        return -np.inf if current_player == 'W' else np.inf
    
    for row in range(current_game.size):
        for col in range(current_game.size):
            if current_game.board[row][col] == '.':
                # Check potential win for current player
                current_game.board[row][col] = current_player
                if current_game.terminal_test(current_player):
                    current_game.board[row][col] = '.'
                    return immediate_win
                current_game.board[row][col] = '.'  
                
                # Check potential win for opponent (block)
                current_game.board[row][col] = opponent_player
                if current_game.terminal_test(opponent_player):
                    potential_score = immediate_block  # Only update score if blocking is necessary.
                current_game.board[row][col] = '.'  

    return potential_score

def defensive_priority_e2(current_game, current_player):
    """Returns the score of the current game state based on the defensive priority evaluation function."""
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    patterns = {'B': {'open_3': 500, 'half_open_3': 200, 'open_4': 5000, 'half_open_4': 2000, 'five': 50000},
                'W': {'open_3': 500, 'half_open_3': 200, 'open_4': 5000, 'half_open_4': 2000, 'five': 50000}}

    opponent = 'W' if current_player == 'B' else 'B'
    size = current_game.size

    for x in range(size):
        for y in range(size):
            if current_game.board[x][y] == '.':
                current_game.board[x][y] = opponent
                if current_game.terminal_test(opponent):
                    current_game.board[x][y] = '.'
                    return -100000
                current_game.board[x][y] = '.'

            if current_game.board[x][y] in ['B', 'W']:
                for dx, dy in directions:
                    for length in range(2, 6):
                        line = [(x + i * dx, y + i * dy) for i in range(length)]
                        if all(0 <= nx < size and 0 <= ny < size for nx, ny in line):
                            stones = [current_game.board[nx][ny] for nx, ny in line]
                            player = current_game.board[x][y]

                            if stones.count(player) == length - 1 and '.' in stones:
                                if all(current_game.board[nx][ny] == '.' for nx, ny in [line[0], line[-1]] if 0 <= nx < size and 0 <= ny < size):
                                    score += patterns[player].get(f'open_{length-1}', 0)
                                else:
                                    score += patterns[player].get(f'half_open_{length-1}', 0)
                            elif stones.count(player) == length and length == 5:
                                score += patterns[player]['five']

                            if stones.count(opponent) == 4 and '.' in stones:
                                score -= 10000

                            if stones.count(current_player) == 4 and '.' in stones:
                                score += 10000

    center = (size // 2, size // 2)
    if current_game.board[center[0]][center[1]] == current_player:
        score += 10000

    return score

def alpha_beta_with_cutoff(current_game, remaining_depth, current_player, alpha, beta):
    """Performs alpha-beta pruning with cutoffs on the game tree. Returns the optimal score and move for the current player."""
    optimal_score = np.inf if current_player != 'W' else -np.inf
    optimal_move = None
    if remaining_depth == 0 or current_game.terminal_test('W') or current_game.terminal_test('B'):
        return score_immediate_moves_e1(current_game, current_player), None # Can be replaced with whichever evaluation function you choose.
    for possible_move in current_game.get_good_moves():
        move_applied = current_game.to_move(possible_move, current_player)
        if move_applied:
            score, _ = alpha_beta_with_cutoff(current_game, remaining_depth - 1, current_game.switch(current_player), alpha, beta)
            current_game.board[possible_move[0], possible_move[1]] = '.'  # Revert move
            if current_player == 'W' and score > optimal_score or current_player != 'W' and score < optimal_score:
                optimal_score, optimal_move = score, possible_move
                alpha, beta = (max(alpha, optimal_score), beta) if current_player == 'W' else (alpha, min(beta, optimal_score))
            if alpha >= beta:
                break
    return optimal_score, optimal_move
