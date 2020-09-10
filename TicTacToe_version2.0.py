from SimpleUserInteraction import position_choice
from Player import Player
from SimpleUserInteraction import chosen_game_list
from SimpleUserInteraction import game_on_choice

playerList = []


def get_player_names():
    count = 1

    while count < 3:
        name = input('Enter player ' + str(count) + ' name: ')
        age = input('Enter player  ' + str(count) + '  age: ')

        playerList.append(Player(name, age, ''))
        count = count + 1

    print('Hello ' + playerList[0].name + ' and ' + playerList[1].name + '. Welcome to Tic Tac Toe\n')

    if playerList[0].age < playerList[1].age:
        print('Since ' + playerList[0].name + ' is younger, ' + playerList[0].name + ' gets to choose the marker.')
        playerList[0].chosenPlayer = True
        return playerList[0]
    else:
        print('Since ' + playerList[1].name + ' is younger, ' + playerList[1].name + ' gets to choose the marker.')
        playerList[1].chosenPlayer = True
        return playerList[1]


def display_board(board):
    clear_output()
    print("Here is the current board")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def clear_output():
    print('\n' * 10)


def get_player_input(chosen_player):
    marker = ''
    player1 = ''
    player2 = ''

    while marker != "X" and marker != "O":
        marker = input(chosen_player.name + ' , choose X or O: ').upper()

        if marker != 'X' and marker != 'O':
            print('Sorry invalid answer')

        if marker == 'X':
            if playerList[0].chosenPlayer:
                playerList[0].marker = 'X'
                playerList[1].marker = 'O'
            else:
                playerList[0].marker = 'O'
                playerList[1].marker = 'X'
        elif marker == 'O':
            if playerList[0].chosenPlayer:
                playerList[0].marker = 'O'
                playerList[1].marker = 'X'
            else:
                playerList[0].marker = 'X'
                playerList[1].marker = 'O'

    if playerList[0].marker == 'X':
        return playerList[0], playerList[1]
    else:
        return playerList[1], playerList[0]


def place_marker(board, marker, position):
    board[position] = marker


def check_win(board):
    is_winner = False

    if ((board[1] == board[2] and board[2] == board[3]) or
            (board[4] == board[5] and board[5] == board[6]) or
            (board[7] == board[8] and board[8] == board[9]) or
            (board[1] == board[4] and board[4] == board[7]) or
            (board[2] == board[5] and board[5] == board[8]) or
            (board[3] == board[6] and board[6] == board[9]) or
            (board[1] == board[5] and board[5] == board[9]) or
            (board[3] == board[5] and board[5] == board[7])):
        is_winner = True
    if range(1, 10) == chosen_game_list:
        print("This game is a Tie")
        game_on_choice()
    return game_on_choice()
    return is_winner


playerToChoose = get_player_names()

test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

player1, player2 = get_player_input(playerToChoose)

display_board(test_board)

winner_mark = ''

while winner_mark == '':
    place_marker(test_board, player1.marker, position_choice(player1.name))
    display_board(test_board)
    if check_win(test_board):
        winner_mark = player1.name
        break

    place_marker(test_board, player2.marker, position_choice(player2.name))
    display_board(test_board)
    if check_win(test_board):
        winner_mark = player2.name
        break

print(winner_mark + ' , you won the game')
# print(check_player_marker())
