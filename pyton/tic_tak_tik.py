
# -------------Global variable ------------
# Display game board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

# If game is still going on
game_still_going = True

# Who is win ? or tie
winner = 's'

# who turn is it
current_player = "X"


def display_board():
    print("")
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |     ' + '1 | 2 | 3')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |     ' + '4 | 5 | 6')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |     ' + '7 | 8 | 9')
    print("")


# play a game of tic tac toe
def play_game():

    # Display initial board
    display_board()

    # the game sill going on
    while game_still_going:

        # check single turn of arbitrary player
        handle_turn(current_player)

        # check if game is over
        check_if_game_over()

        # change the player values
        filp_player()

        # the game end
        if winner == "X" or winner == "O":
            print(winner + ' won.')
        elif winner == None:
            print()


# handle a single turn arbitrary player
def handle_turn(player):
    print(player + " s' turn")
    position = input('Chose your position into 1-9:')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invaid input .Chosen your position into 1-9")

        position = int(position) - 1

        if board[position] == '_':
            valid = True
        else:
            print("you cant go there. go again")

    board[position] = player
    display_board()


# check game is over
def check_if_game_over():
    check_if_winner()
    check_if_tie()


def check_if_winner():
    # set of global values
    global winner

    # check row
    row_winner = check_row()

    # check colume
    colume_winner = check_colume()

    # check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        # There was a winner
        winner = row_winner

    elif colume_winner:
        # There was a winner
        winner = colume_winner
    elif diagonal_winner:
        # There was a winner
        winner = diagonal_winner

    else:
        winner = None
    return


def check_row():
    # set up global variable
    global game_still_going

    # check if any of the have same values that means winner
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'

    if row_1 or row_2 or row_3:
        game_still_going = False

    # RETURN THE winner ( X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_colume():
    # set up global variable
    global game_still_going

    # check if any of the have same values that means winner
    colume_1 = board[0] == board[3] == board[6] != '_'
    colume_2 = board[1] == board[4] == board[7] != '_'
    colume_3 = board[2] == board[5] == board[8] != '_'

    if colume_1 or colume_2 or colume_3:
        game_still_going = False

    # RETURN THE winner ( X or O)
    if colume_1:
        return board[0]
    elif colume_2:
        return board[1]
    elif colume_3:
        return board[2]
    return


def check_diagonal():
    # set up global variable
    global game_still_going

    # check if any of the have same values that means winner
    diagonal_1 = board[0] == board[4] == board[8] != '_'
    diagonal_2 = board[2] == board[4] == board[6] != '_'

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # RETURN THE winner ( X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    if '_' not in board:
        game_still_going = False
        return True
    else:
        return False


def filp_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


# ------ Game start excutions ------
play_game()
