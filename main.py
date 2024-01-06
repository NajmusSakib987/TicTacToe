def main():
    game_board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    print("\nWelcome to Tic Tac Toe!\n")
    game_running = True
    sign = "X"
    while game_running:
        print_board(game_board)
        position = user_input()
        #sign switching
        if sign == "X":
            sign = 'O'
        else:
            sign = "X"

        input_assign(position, game_board, sign)

        if winner_found(game_board):
            print_board(game_board)
            print(f'\nGame over, Winner is "{sign}"')
            game_running = False
        elif tie(game_board):
            print_board(game_board)
            print(f'\nGame is tied')
            game_running = False

#checking for tie
def tie(board):
    if not any('-' in row for row in board):
        if any('X' in row and 'O' in row for row in board):
            return True
#checking for winner
def winner_found(board):
    if row_matched(board) or column_matched(board) or diagonal_matched(board):
        return True
    else:
        return False

#the game board
def print_board(board):
    for row in board:
        for column in row:
            print("| "+ column + " |", end =' ')
        print()

#winning conditions
def row_matched(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != '-':
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != '-':
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != '-':
        return True
    else:
        return False
def column_matched(board):
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != '-':
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '-':
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != '-':
        return True
    else:
        return False
def diagonal_matched(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True
    else:
        return False
def user_input():
    try:
        position = int(input('\nEnter a position between 1 to 9: '))
        return position
    except ValueError:
        print('\nTry again! Enter a value between 1 to 9!\n')


def valid(user):
    if user != None:
        if 1 <= user <= 9:
            return True
        else:
            return False
    else:
        return False

def input_assign(user,board,sign):
    if valid(user):
        new_sign = sign
        c_user = user - 1

        if 0 <= c_user <= 2 and board[0][c_user] == '-':
            board[0][c_user] = f'{new_sign}'
        elif 3 <= c_user <= 5 and board[1][c_user - 3] == '-':
            board[1][c_user - 3] = f'{new_sign}'
        elif 6 <= c_user <= 8 and board[2][c_user - 6] == '-':
            board[2][c_user - 6] = f'{new_sign}'
        else:
            print('\nThe place is already taken\n')
    else:
        print('\nInput must be between 1 and 9\n')


main()