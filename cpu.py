# cpu.py
import random

def cpu_move(board, difficulty):
    if difficulty == "easy":
        return random_move(board)
    elif difficulty == "hard":
        return best_move(board)

def random_move(board):
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
    return random.choice(empty) if empty else None

def best_move(board):
    best_score = float('inf')
    best = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'O'
                score = minimax(board, 0, True)
                board[row][col] = ''
                if score < best_score:
                    best_score = score
                    best = (row, col)
    return best

def minimax(board_state, depth, is_maximizing):
    from main_pygame import check_win, board_full

    if check_win('X'):
        return 1
    if check_win('O'):
        return -1
    if board_full():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board_state[row][col] == '':
                    board_state[row][col] = 'X'
                    score = minimax(board_state, depth + 1, False)
                    board_state[row][col] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board_state[row][col] == '':
                    board_state[row][col] = 'O'
                    score = minimax(board_state, depth + 1, True)
                    board_state[row][col] = ''
                    best_score = min(score, best_score)
        return best_score