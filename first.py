import random
import time

#prelims
player_name = input('Enter your name to start the Game: ')

print(f"Welcome to the Tic Tac Toe Game v 1.0.0 {player_name}")
print('We hope you will enjoy playing the game!!')
h_or_t = ['heads', 'tails']
head_tails = input(f"Before we start you need to choose between heads or tails: ")

h_or_t_selection = random.choice(h_or_t)
time.sleep(3)
print(f'The choice is {h_or_t_selection}')
if h_or_t_selection == head_tails:
    print('You will start first')
else:
    print('You are second to play')



choice_x_o = input("Select between x and o to start to play: ")
if choice_x_o == 'x':
    player_pawn = 'x'
    print(f'You have selected {player_pawn}')
else:
    player_pawn='o'
    print(f'You have selected {player_pawn}')

player_two = 'cpu'


board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for i in board:
    print(i)

while True:

    print(f"Start by placing {player_pawn} in one of the cells")
    select = int(input(f"Enter the number that the '{player_pawn}' would go to: "))
    if select == 1:
        board[0][0] = player_pawn
    elif select == 2:
        board[0][1] = player_pawn
    elif select == 3:
        board[0][2] = player_pawn
    elif select == 4:
        board[1][0] = player_pawn
    elif select == 5:
        board[1][1] = player_pawn
    elif select == 6:
        board[1][2] = player_pawn
    elif select == 7:
        board[2][0] = player_pawn
    elif select == 8:
        board[2][1] = player_pawn
    elif select == 9:
        board[2][2] = player_pawn

    for i in board:
        print(i)

    if board[0][0] and board[0][1] and board[0][2] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[0][0] and board[1][0] and board[2][0] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[2][0] and board[2][1] and board[2][2] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[0][2] and board[1][2] and board[2][2] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[1][0] and board[1][1] and board[1][2] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[0][0] and board[1][1] and board[2][2] == player_pawn:
        print('Congratulations!! You won the game!!')
        break
    elif board[0][2] and board[1][2] and board[2][0] == player_pawn:
        print('Congratulations!! You won the game!!')
        break





    
    