# Игра "Крестики-Нолики"

from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
def player_input():
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    marker=''
    while not (marker =='X' or  marker =='О'):
        marker = input('Игрок1 - выберите X или О:').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    (board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)
def choose_first():
    flip = random.randint(0, 1)
    if flip==0:
        return 'Игрок1'
    else:
        return 'Игрок2'
def space_check(board, position):
    return board[position] ==' '
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Укажите поле: (1-9)'))
    return position
def replay():
    choice = input('Хотите играть снова? Введите Yes или No')
    return choice == 'Yes'

print('Добро пожаловать в игру Крестики-Нолики')

while True:
    the_board=[' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn +' ходит первый')
    play_game = input('Вы готовы играть? Yer or No')
    
    if play_game == 'Yes':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'Игрок1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Игрок1 выиграл')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on=False
                else:
                    turn == 'Игрок2'
                    
        
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Игрок2 выиграл')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on=False
                else:
                    turn == 'Игрок1'
        
    
    if not replay():
        break