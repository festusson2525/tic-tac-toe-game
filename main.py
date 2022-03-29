import random

def display_board(board):
    # this function is going to display the tic-tac-toe board
    print('\n' * 100)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- - - - -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- - - - -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    # this function assign X or O to each player on the board
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def player_marker(board, marker, position):
    # this is a function that assigns players marker to the position they choose in the board
    board[position] = marker

def win_check(board, mark):
    # this is a function to check all rows for matching markers
    # check all rows for matching markers
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            # check all columns for matching markers
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            # check all diagonals for matching markers
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def choose_first():
    # this is a function that randomly select either player 1 or player 2
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    # this is a function to check for empty space in the board in-case the next player still have a turn
    return board[position] == ' '

def full_board_check(board):
    # this is a function that check if the board is full or not
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if we return True
    return True

def player_choice(board):
    # this is a function that asks the next player to choose a position from 1 to 9
    # and uses the position from function space_check to know if it is in a free position
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position from 1 - 9: '))
    return position

def replay():
    # this is a function that checks if the players want to play again or not
    choice = input("Play again? Yes or No ")
    return choice == 'Yes'


# We will need while loop to keep running the game
print('Welcome to TIC TAC TOE!... made by Godstime Festus (twitter: @godstimefestus_)')
while True:
    # Begin the Game !
    # Set Everything up ( The Board, who is first player, assign marker to each player (X or O))
    the_board = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Yes or No ')
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)

            # player 1 will choose a position
            position = player_choice(the_board)

            # player 1 will place a marker on the position
            player_marker(the_board, player1_marker, position)

            # check if player_1 won the game
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON !!! ')
                game_on = False
            else:
                # check if it is a tie (No winner)
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME... ')
                    break
                else:
                    # next player's turn
                    turn = 'Player 2'

        else:
            # show the board
            display_board(the_board)

            # player 2 will choose a position
            position = player_choice(the_board)

            # player 2 will place a marker on the position
            player_marker(the_board, player2_marker, position)

            # check if player_2 won the game
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON !!! ')
                game_on = False

            else:
                # check if it is a tie (No winner)
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME... ')
                    break
                else:
                    # next player's turn
                    turn = 'Player 1'

    if not replay():
        break
