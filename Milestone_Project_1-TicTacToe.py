from IPython.display import clear_output
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

    marker = ''
    global player1
    global player2

    # Keep asking player 1 to choose if neither 'X' or 'O' are passed as arguments.
    while(marker != 'X' and marker != 'O'):
        marker = raw_input('Player 1, would you like to play with X or O? \n')

    # Assign Player 2 the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1, player2)

def place_marker(board, marker, position):
    del board[position]
    board.insert(position,marker)
    #print("%s turn", player)
    #display_board(board)
    #return board

def win_check(board, marker):
    if (board[1] == board[2] == board[3] == marker):
        print'1'
        return True
    elif(board[4] == board[5] == board[6] == marker):
        print'2'
        return True
    elif(board[7] == board[8] == board[9] == marker):
        print'3'
        return True
    elif(board[1] == board[4] == board[7] == marker):
        print'4'
        return True
    elif(board[2] == board[5] == board[8] == marker):
        print'5'
        return True
    elif(board[3] == board[6] == board[9] == marker):
        print'6'
        return True
    elif(board[1] == board[5] == board[9] == marker):
        print'7'
        return True
    elif(board[7] == board[5] == board[3] == marker):
        print'8'
        return True
    else:
        return False


#win_check(test_board, 'X')

def choose_first():
    player_number = random.randint(1,2)
    return 'Player #{}'.format(player_number)


def space_check(board, position):
    if board[position] in ["X", "O"]:
        return False    # Used
    else:
        return True     # Available

def full_board_check(board):
    if board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] in ["X","O"]:
        return True # Board is Full.
    else:
        return False # Board is NOT full yet

def player_choice(board, player_marker):
    position = int(raw_input('Please select your next position (1 - 9): '))
    available = space_check(board,position)
    if available:
        place_marker(board,player_marker,position)
        return True
    else:
        return False

def replay():
    play_again = raw_input('Would you like to play again? (Y, N): ')
    if play_again.lower()[0] == 'y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe Game...')

#game_on = True
while True:
    my_board = [' '] * 10
    p1, p2 = player_input()

    player = choose_first()
    print(player + " will go first.")

    play_game = raw_input("Are you ready to play? (Yes or No)")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        break

    while game_on:
        if player == 'Player #1':
            #Player 1 turn
            display_board(my_board)
            position = player_choice(my_board, p1)
            if not position:
                print('Position is taken... please select another one')
                continue
            if win_check(my_board,p1):
                display_board(my_board)
                print("Congratulations! You have won the game")
                #if not replay():
                 #   print("Thanks for playing\n\n\n")
                  #  break
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print('The game is a draw!')
                    break
                else:
                    player = 'Player #2'
                    print(player + ' turn')
        else:
            #Player 2 turn
            display_board(my_board)
            position = player_choice(my_board,p2)
            if not position:
                print('Position is taken... please select another one ')
                continue
            if win_check(my_board,p2):
                display_board(my_board)
                print("Congratulations! You have won the game")
                #if not replay():
                 #   print("Thanks for playing\n\n\n")
                  #  break
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print("The game is a draw!")
                    break
                else:
                    player = 'Player #1'
                    print(player + ' turn')

            #print('If this is shown, then after the game_on variable has being set to False, it will still run code beneath')
    if not replay():
        print("Thanks for playing.")
        break
'''


    if player == 'Player #1':
        print("Player # 1 goes first")
        isAvailable = player_choice(my_board,p1)
        if isAvailable:
            print('Continuing...')
        else:
            print('Position is taken already, please choose other position.')
            continue

    else:
        print("Player # 2 goes first")
        isAvailable = player_choice(my_board,p2)
        if isAvailable:
            pass
        else:
            print('Position is taken already, please choose other position.')
            continue


'''


