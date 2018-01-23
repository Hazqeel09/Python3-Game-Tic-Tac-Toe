# Run this code in your command prompt for Windows


import random
import os
import time


def clear():
    '''
    To clear the command prompt
    '''
    os.system('cls')


def player_name():
    '''
    To get players name
    '''
    global play1
    global play2
    print('\nPlayer 1 will use X while Player 2 will use O \n')
    play1 = input('Player 1 name: ')
    play2 = input('Player 2 name: ')

    print('\nHye ' + play1)
    print('Hye ' + play2 + '\n')


def choose_turn():
    '''
    To choose turn for players
    '''
    x = random.randint(1, 3)
    global first
    global second
    global isi_1
    global isi_2

    if x == 1:
        first = play1
        isi_1 = 'X'
        second = play2
        isi_2 = 'O'
        print(play1 + ' goes first \n')
    else:
        first = play2
        isi_1 = 'O'
        second = play1
        isi_2 = 'X'
        print(play2 + ' goes first \n')


def display_board(board):
    '''
    To display the tic tac toe board
    '''
    clear()
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("------------")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("------------")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n')


def player1_choice(board):
    '''
    To take and validate input from first player
    '''
    global move1
    move1 = ' '
    move1 = input('Player ' + first + ' please give your input (1-9): ')

    while move1 not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move1)):
        print('Your input is invalid \n')
        move1 = input('Player ' + first + ' please give your input (1-9): ')

    return int(move1)


def player2_choice(board):
    '''
    To take and validate input from second player
    '''
    global move2
    move2 = ' '
    move2 = input('Player ' + second + ' please give your input (1-9): ')

    while move2 not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move2)):
        print('Your input is invalid \n')
        move2 = input('Player ' + second + ' please give your input (1-9): ')

    return int(move2)


def marking1(board, move1, isi_apa):
    '''
    To display the input from first player
    '''
    global move
    global isi_apa1
    move = move1
    isi_apa1 = isi_1
    board[move] = isi_apa
    return int(move)


def marking2(board, move2, isi_apa):
    '''
    To display the input from second player
    '''
    global isi_apa2
    global move
    move = move2
    isi_apa2 = isi_2
    board[move] = isi_apa
    return int(move)


def win_check(board, isi_apa):
    '''
    To check board if any player had win the game
    '''
    return ((board[1] == isi_apa and board[2] == isi_apa and board[3] == isi_apa) or
            (board[1] == isi_apa and board[4] == isi_apa and board[7] == isi_apa) or
            (board[1] == isi_apa and board[5] == isi_apa and board[9] == isi_apa) or
            (board[2] == isi_apa and board[5] == isi_apa and board[8] == isi_apa) or
            (board[4] == isi_apa and board[5] == isi_apa and board[6] == isi_apa) or
            (board[7] == isi_apa and board[8] == isi_apa and board[9] == isi_apa) or
            (board[3] == isi_apa and board[5] == isi_apa and board[7] == isi_apa) or
            (board[3] == isi_apa and board[6] == isi_apa and board[9] == isi_apa))


def space_check(board, move):
    '''
    To check the board if it is empty or filled
    '''
    return board[move] == ' '


def full_board(board):
    '''
    To check if the board is already full
    '''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def replay():
    '''
    To let players play again
    '''
    return input('Do you want to play another round (y/n) ? : ').lower().startswith('y')


while True:
    clear()  # Clear the board
    print('Welcome to Tic Tac Toe \n')
    TheBoard = [' '] * 10
    player_name()  # Get player name
    choose_turn()  # Random turn
    time.sleep(1)  # Pause for one second
    print('Ready!!!')
    time.sleep(1)
    print('Set!!!')
    time.sleep(1)
    print('Go!!!')
    time.sleep(1)

    while True:  # First player turns
        display_board(TheBoard)  # Clear command prompt and display the board
        move1 = player1_choice(TheBoard)  # Receive first player input
        isi_apa = isi_1  # assigning isi_apa with 'X' or 'O' depends on the random turn result
        marking1(TheBoard, move1, isi_apa)

        if win_check(TheBoard, isi_apa):  # Check if first player win
            display_board(TheBoard)
            print('Congratulation Player ' + first + ' WIN!!! \n')
            print('Player ' + second + ' DO NOT give up!!! \n')
            break

        elif full_board(TheBoard):  # Check if board is full
            display_board(TheBoard)
            print('It is a draw \n')
            break

        else:  # Second player turns
            display_board(TheBoard)
            move2 = player2_choice(TheBoard)
            isi_apa = isi_2
            marking2(TheBoard, move2, isi_apa)

            if win_check(TheBoard, isi_apa):  # Check if second player win
                display_board(TheBoard)
                print('Congratulation Player ' + second + ' WIN!!! \n')
                print('Player ' + first + ' DO NOT give up!!! \n')
                break

            elif full_board(TheBoard):  # Check if the board is full
                display_board(TheBoard)
                print('It is a draw \n')
                break

    if not replay():  # Ask for a replay
        print('Thanks for playing')
        break