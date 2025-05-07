import pygame
import sys
from cpu import cpu_move

# Initialize pygame
pygame.init()
FONT = pygame.font.SysFont('Arial', 28)

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 4
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 4
X_WIDTH = 12
SPACE = SQUARE_SIZE // 4

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (66, 66, 255)
O_COLOR = (255, 66, 66)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(WHITE)

# Game board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
difficulty = "easy"
winner_text = ""

def draw_message(text):
    msg = FONT.render(text, True, (20, 20, 20))
    rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(msg, rect)

# Functions to draw
def draw_lines():
    for i in range(1, BOARD_ROWS):
        # Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # Vertical
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_marks():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            mark = board[row][col]
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            if mark == 'X':
                # Draw X
                offset = SPACE
                pygame.draw.line(screen, X_COLOR, (center[0]-offset, center[1]-offset), (center[0]+offset, center[1]+offset), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (center[0]+offset, center[1]-offset), (center[0]-offset, center[1]+offset), X_WIDTH)
            elif mark == 'O':
                # Draw O
                pygame.draw.circle(screen, O_COLOR, center, CIRCLE_RADIUS, X_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def is_empty(row, col):
    return board[row][col] == ''

def check_win(player):
    # Horizontal, vertical, and diagonal checks
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

def board_full():
    return all(board[row][col] != '' for row in range(3) for col in range(3))

# def cpu_move():
#     empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
#     return random.choice(empty_cells) if empty_cells else None

def restart():
    global board, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    screen.fill(WHITE)
    draw_lines()
    game_over = False

# Initial draw
draw_lines()
game_over = False
player_turn = True  # Player = 'X', CPU = 'O'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and player_turn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if is_empty(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, 'X')
                    if check_win('X'):
                        winner_text = "You Win!"  # for player
                        print("Player wins!")
                        game_over = True
                    elif board_full():
                        winner_text = "It's a tie!"  # for tie
                        print("It's a tie!")
                        game_over = True
                    else:
                        player_turn = False

        # CPU turn
        if not game_over and not player_turn:
            pygame.time.delay(500)
            move = cpu_move(board, difficulty)
            if move:
                row, col = move
                mark_square(row, col, 'O')
                if check_win('O'):
                    game_over = True
                    winner_text = "CPU Wins!"
                elif board_full():
                    game_over = True
                    winner_text = "It's a tie!"
                else:
                    player_turn = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                winner_text = ""
                restart()

            if event.key == pygame.K_d:
                difficulty = "easy" if difficulty == "hard" else "hard"
                print(f"Difficulty set to: {difficulty}")

    draw_marks()
    if game_over:
        draw_message(winner_text + "  |  Press R to Restart")
    pygame.display.update()