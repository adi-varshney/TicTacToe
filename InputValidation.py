def user_choice():
    choice = "Wrong"

    while not choice.isdigit() or not is_acceptable(choice):
        choice = input("Please enter a number(1-10): ")
        if not choice.isdigit():
            print("Sorry that is not a number")
        elif not is_acceptable(choice):
            print("Sorry, that is not a number within 1-10")

    return int(choice)


def is_acceptable(xyz):
    acceptable_values = range(1, 11)
    num = int(xyz)
    if num not in acceptable_values:
        return False
    else:
        return True


# print(user_choice())
