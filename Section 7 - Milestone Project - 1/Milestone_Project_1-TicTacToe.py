#from IPython.display import clear_output
import random

#my_board = ['#','1','2','3','4','5','6','7','8','9']
test_board = ['#','X','O','X','O','X','O','X','O','X']
player1 = ''
player2 = ''

def display_board(board):
    print("-" * 50)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-----")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-----")
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''
    global player1
    global player2

    # Keep asking player 1 to choose if neither 'X' or 'O' are passed as arguments.
    while(marker != 'X' and marker != 'O'): # also: while not (marker == 'X' or marker == '0'):
        marker = raw_input('Player 1, would you like to play with X or O? \n').upper()

    # Assign Player 2 the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1, player2)

    # We could've simplified above by only putting:
    # if marker = 'X':
    #   return('X', '0')
    # else:
    #   return ('O', 'X')

def place_marker(board, marker, position):
    # del board[position]           -> Not so clever. I did it.
    # board.insert(position,marker) -> Not so clever. I did it.
    # Better way:
    board[position] = marker

    #print("%s turn", player)
    #display_board(board)
    #return board

def win_check(board, marker):
    if (board[1] == marker and board[2] == marker and board[3] == marker): # ROWS
        print'1'
        return True
    elif(board[4] == marker and board[5] == marker and board[6] == marker): # ROWS
        print'2'
        return True
    elif(board[7] == marker and board[8] == marker and board[9] == marker): # ROWS
        print'3'
        return True
    elif(board[1] == marker and board[4] == marker and board[7] == marker): # COLUMNS
        print'4'
        return True
    elif(board[2] == marker and board[5] == marker and board[8] == marker): # COLUMNS
        print'5'
        return True
    elif(board[3] == marker and board[6] == marker and board[9] == marker): # COLUMNS
        print'6'
        return True
    elif(board[1] == marker and board[5] == marker and board[9] == marker): # DIAGONALS
        print'7'
        return True
    elif(board[7] == marker and board[5] == marker and board[3] == marker): # DIAGONALS
        print'8'
        return True
    else:
        return False


#win_check(test_board, 'X')

def choose_first():
    player_number = random.randint(1,2)
    return 'Player #{}'.format(player_number)


def space_check(board, position):
    # If we use below way, it won't work with full_board_check() function.

    #if board[position] in ["X", "O"]:
    #    return False    # Used
    #else:
    #    return True     # Available

    # Or simply:
    return board[position] == ' ' # True if empty, False if taken.

def full_board_check(board):
    # BELOW WAY TO CHECK, IS NOT SO CLEVER.

    # if board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] in ["X","O"]:
        #return True # Board is Full.
    #else:
        #return False # Board is NOT full yet

    # A MORE CLEVER WAY:
    for i in range(1,10): # Starting with 1, up to (but not including) 10.
        if space_check(board, i):
            return False # Board is NOT full yet

    return True # Board is Full

    '''
    Another way to achieve same as above is:
    
    if " " in board[1:]: 
        return False
    else:
        return True
    '''

def player_choice(board, player_marker):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(raw_input('Choose a position: (1 - 9): '))

    return position
    #available = space_check(board,position)
    #if available:
    #    place_marker(board,player_marker,position)
    #    return True
    #else:
    #    return False

def replay():
    play_again = raw_input('Would you like to play again? (Y, N): ')
    if play_again.lower()[0] == 'y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe Game...')

#game_on = True
while True:
    # -----> Play the game.

    my_board = [' '] * 10
    p1_marker, p2_marker = player_input() # -----> X or O markers set for players.

    player = choose_first() # ----> Who's first, Player 1 or Player 2?
    print(player + " will go first.")

    play_game = raw_input("Are you ready to play? (Yes or No)") # ----> Ready to play?

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        #break

    while game_on: # ----> If ready to play, begin

        if player == 'Player #1':  # -----> Player 1 turn
            print("Player 1 turn...")
            display_board(my_board) # ----> Show the board.
            position = player_choice(my_board, p1_marker) # ----> Choose a position.
            place_marker(my_board, p1_marker, position) # -----> Place the marker on the position.

            if win_check(my_board, p1_marker): # ----> Check if player 1 won
                display_board(my_board)
                print("Player 1 has won!")
                game_on = False # ----> Will break out from the inner (while game_on) while loop; going to the "if not replay() function"

            if full_board_check(my_board): # ----> It player 1 hasn't won yet, then check if Board is full - If so, it means it's a tie (or that P2 won).
                display_board(my_board)
                print("Tie Game!")
                game_on = False # ----> Is the same as putting a "break" statement.
            else: # ----> Board is still not full
                player = 'Player #2' # ---> Since game hasn't won, nor is tied, is player's 2 turn.

        else: # ----> Player 2 turn.
            print("Player 2 turn...")
            display_board(my_board)  # ----> Show the board.
            position = player_choice(my_board, p1_marker)  # ----> Choose a position.
            place_marker(my_board, p2_marker, position)  # -----> Place the marker on the position.

            if win_check(my_board, p2_marker):  # ----> Check if player 2 won
                display_board(my_board)
                print("Player 2 has won!")
                game_on = False  # ----> Will break out from the inner (while game_on) while loop; going to the "if not replay() function"

            if full_board_check(my_board):  # ----> It player 2 hasn't won yet, then check if Board is full - If so, it means it's a tie (or that P1 won).
                display_board(my_board)
                print("Tie Game!")
                game_on = False  # ----> Is the same as putting a "break" statement.
            else:  # ----> Board is still not full
                player = 'Player #1'  # ---> Since game hasn't won, nor is tied, is player's 1 turn.

    if not replay(): # ---> If one of the players win, or the game is a tied, ask user if he/she wants to play again.
        print("Thanks for playing.")
        break



