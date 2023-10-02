import random
import time

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Preliminaries
player_name = input('Enter your name to start the Game: ')

print(f"Welcome to the Tic Tac Toe Game v 2.0.0, {player_name}!")
print('We hope you will enjoy playing the game!!')

h_or_t = ['heads', 'tails']
head_tails = input(f"Before we start, you need to choose between heads or tails: ")

h_or_t_selection = random.choice(h_or_t)
time.sleep(3)
print(f'The choice is {h_or_t_selection}')
if h_or_t_selection == head_tails:
    print('You will start first')
    player_one_pawn = 'X'
    player_two_pawn = 'O'
else:
    print('You are second to play')
    player_one_pawn = 'O'
    player_two_pawn = 'X'

print(f"{player_name}, you are '{player_one_pawn}'")
print(f"CPU is '{player_two_pawn}'")

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Main game loop
while True:
    # Player's turn
    print_board(board)
    while True:
        try:
            select = int(input(f"Enter the number where you want to place '{player_one_pawn}': "))
            row = (select - 1) // 3
            col = (select - 1) % 3
            if 1 <= select <= 9 and board[row][col] == " ":
                board[row][col] = player_one_pawn
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

    # Check if the player wins
    if check_win(board, player_one_pawn):
        print_board(board)
        print(f'Congratulations, {player_name}! You won!')
        break

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        print_board(board)
        print("It's a tie!")
        break

    # CPU's turn
    print("CPU is thinking...")
    time.sleep(2)
    while True:
        select = random.randint(1, 9)
        row = (select - 1) // 3
        col = (select - 1) % 3
        if board[row][col] == " ":
            board[row][col] = player_two_pawn
            break

    # Check if the CPU wins
    if check_win(board, player_two_pawn):
        print_board(board)
        print('CPU wins! Better luck next time, {player_name}!')
        break