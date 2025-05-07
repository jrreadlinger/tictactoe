import random

# Display the game board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check for a win
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

# Check for a tie
def is_tie(board):
    return all(cell != ' ' for cell in board)

# Get player's move
def player_move(board):
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("Cell already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number 1-9.")

# CPU chooses a random move
def cpu_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(empty_cells)

# Main game loop
def play_game():
    board = [' '] * 9
    current_player = 'X'  # Player is X, CPU is O

    print("Welcome to Tic-Tac-Toe!")
    display_board([str(i+1) for i in range(9)])  # Show board positions

    while True:
        display_board(board)

        if current_player == 'X':
            move = player_move(board)
        else:
            print("CPU is making a move...")
            move = cpu_move(board)

        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            winner = "You" if current_player == 'X' else "CPU"
            print(f"{winner} win!")
            break

        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()