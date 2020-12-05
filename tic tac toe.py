msg = """
+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+ +-+-+-+
|w|e|l|l|c|o|m|e| |t|o| |t|i|c| |t|a|c| |t|o|e|
+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+ +-+-+-+
"""
print('\x1b[1;33;29m' + msg + '\x1b[0m')
msg = 'press the number were you want to put the cursor\npress enter to put your mark\npress (q) anytime to exit from the game!\n'
print('\x1b[0;31;29m' + msg + '\x1b[0m')

# -------- Global variables ----------
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
game_state = True
current_player = 'x'


def display_board():
    """display the board to the screen"""
    print('\x1b[1;36;29m' +
          f'{board[0]}|{board[1]}|{board[2]}'+'\x1b[0;36;29m'+"\t1|2|3")
    print('\x1b[1;36;29m' +
          f'{board[3]}|{board[4]}|{board[5]}'+'\x1b[0;36;29m'+"\t4|5|6")
    print('\x1b[1;36;29m' +
          f'{board[6]}|{board[7]}|{board[8]}'+'\x1b[0;36;29m'+"\t7|8|9")
    print('\x1b[0m')


def handle_turn(player):
    """handle everything of a player's turn"""
    global board
    position = input('\x1b[0;34;29m' + '>>>' + '\x1b[0m')
    valid = False
    while not valid:
        # make sure input is valid
        while position not in [str(x) for x in range(1, 10)]:
            position = input('\x1b[0;34;29m' +
                             'choose from 1-9\n>>>' + '\x1b[0m')

        # Get correct index in our board list
        position = int(position)-1

        if board[position] == '-':
            valid = True
        else:
            print('\x1b[0;31;29m' +
                  "it's already filled choose another one" + '\x1b[0m')
    # put the piece in the board
    board[position] = player

    # show updated board
    display_board()


def check_game_over():
    """check if the game got a winner or a tie"""
    global game_state
    # row check
    for i in range(0, 7, 3):
        if (board[i] == board[i+1] == board[i+2] != '-'):
            game_state = False
            return '\x1b[1;31;29m'+f'{board[i]}' + '\x1b[0m' + " won"

    # column check()
    for i in range(0, 3):
        if (board[i] == board[i+3] == board[i+6] != '-'):
            game_state = False
            return '\x1b[1;31;29m'+f'{board[i]}' + '\x1b[0m' + " won"

    # diagonal check()
    if (board[0] == board[4] == board[8] != '-') or (board[2] == board[4] == board[6] != '-'):
        game_state = False
        return '\x1b[1;31;29m'+f'{board[4]}' + '\x1b[0m' + " won"

    if '-' not in board:
        game_state = False
        return "it's a " + '\x1b[1;31;29m'+'Tie'+'\x1b[0m'


def flip_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'


def play_game():
    # show the initial game board
    display_board()
    winner = None
    # loop until the game stops(winner or tie)
    while game_state:
        # handle a turn
        handle_turn(current_player)

        # check for winner/tie and decide game_state
        winner = check_game_over()

        # flip the player
        flip_player()

    # printing the winner or tie
    print(winner)


# ------------ Start Execution -------------
play_game()
