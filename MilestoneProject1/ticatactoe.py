import random
from turtle import pos, position

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker !='O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker ==  'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or 
            (board[4]==marker and board[5]==marker and board[6]==marker) or 
            (board[7]==marker and board[4]==marker and board[1]==marker) or 
            (board[8]==marker and board[5]==marker and board[2]==marker) or 
            (board[9]==marker and board[6]==marker and board[3]==marker) or 
            (board[1]==marker and board[2]==marker and board[3]==marker) or 
            (board[7]==marker and board[5]==marker and board[3]==marker) or 
            (board[9]==marker and board[5]==marker and board[1]==marker))

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))

    return position

def replay():
    choice=input("Play again? Enter Yes or No ")
    
    return choice=='Yes'

print("Welcome to Tic Tac Toe")

while True:
    the_board=[' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()

    print(turn+" will go first")

    play_game = input('Ready to play? y or n ')

    if play_game=='y':
        game_on= True
    else:
        game_on=False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!!")
                game_on=False
            elif full_board_check(the_board):
                display_board(the_board)
                print("Tie game!")
                break
            else:
                turn='Player 2'
        else:
            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!!")
                game_on=False
            elif full_board_check(the_board):
                display_board(the_board)
                print("Tie game!")
                break
            else:
                turn='Player 1'

    if not replay():
        break