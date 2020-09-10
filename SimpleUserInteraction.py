
chosen_game_list = []


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


def position_choice(pmarker):
    if range(1, 10) in chosen_game_list:
        print("This game was a Tie")
        game_on_choice()
        if game_on_choice() == False:
            return False
        else:
            return True

    choice = "wrong"

    while choice not in range(1, 10) or choice not in chosen_game_list:
        choice = int(input(pmarker + ", Pick a position (1-9): "))

        if choice not in range(1, 10):
            print("sorry, invalid choice ")
        elif choice not in chosen_game_list:
            chosen_game_list.append(choice)
            if chosen_game_list in range(1, 10):
                game_on_choice()

        elif choice in chosen_game_list:
            if range(1, 10) in chosen_game_list:
                print("This game was a Tie")
                game_on_choice()
                if game_on_choice() == False:
                    break

            print("Sorry " + pmarker + ", that position is already taken")
            choice = "wrong"

    return choice


def replacement_choice(game_list, position):
    user_placement = input("Type a string to replace the position: ")
    game_list[position] = user_placement
    return game_list


def game_on_choice():
    choice = "wrong"
    while choice not in ['Y', 'N']:
        choice = input("Want to keep playing? (Y/N): ")
        if choice not in ['Y', 'N']:
            print("sorry, invalid choice ")
    if choice == "Y":
        return True
    else:
        return False

# while game_on_choice():
#     print(replacement_choice(game_list, position_choice()))
# print(position_choice())
# print(replacement_choice(game_list, position_choice()))
# print(game_on_choice())
