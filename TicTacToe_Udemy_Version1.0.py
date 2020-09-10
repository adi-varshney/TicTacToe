import random


def clear_output():
    print('\n' * 3)


def get_player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return 'X', "O"
    else:
        return 'O', "X"


def display_board(board):
    clear_output()
    print("Here is the current board")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def replay():
    choice = input('Play again? Enter Yes or No')
    return choice == 'Yes'


# player1_marker, player2_marker = get_player_input()
print('Welcome to Tic Tac Toe!')
while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = get_player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N ')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a tie')
                    break
                else:
                    turn = 'player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a tie')
                    break
                else:
                    turn = 'player 1'
    if not replay():
        break
# test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# display_board(test_board)
# print(win_check(test_board, 'X'))
# print(win_check(test_board, 'O'))
