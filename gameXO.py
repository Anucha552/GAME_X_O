import os


def start_game():
    global table_X_O
    global number_input
    global select_X_O
    global open_logo
    global text_error
    global exit_game

    table_X_O = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    number_input = ""
    select_X_O = ""
    open_logo = True
    text_error = ""
    exit_game = False


def show_X_O():

    t = ""

    for r in range(len(table_X_O)):
        t = (
            t
            + "\n "
            + table_X_O[r][0]
            + " | "
            + table_X_O[r][1]
            + " | "
            + table_X_O[r][2]
        )
        if r < 2:
            t = t + "\n---+---+---"

    return t


def check_X_O():

    channel = 0
    text_game_over = "NO"
    X_O_row = ["", "", ""]
    X_O_column = ["", "", ""]
    X_O_diagonal = ["", ""]

    for r in range(3):
        for c in range(3):

            if table_X_O[r][c] != " ":
                channel = channel + 1

            X_O_row[r] = X_O_row[r] + table_X_O[r][c]
            X_O_column[r] = X_O_column[r] + table_X_O[c][r]

            if r == 0:
                X_O_diagonal[r] = X_O_diagonal[r] + table_X_O[c][c]

            if r == 1:
                X_O_diagonal[r] = X_O_diagonal[r] + table_X_O[c][2 - c]

    if channel != 9:
        for r in X_O_row:
            if r == "XXX":
                text_game_over = "GAME OVER\n  X WIN"
            elif r == "OOO":
                text_game_over = "GAME OVER\n  O WIN"

        for c in X_O_column:
            if c == "XXX":
                text_game_over = "GAME OVER\n  X WIN"
            elif c == "OOO":
                text_game_over = "GAME OVER\n  O WIN"

        for d in X_O_diagonal:
            if d == "XXX":
                text_game_over = "GAME OVER\n  X WIN"
            elif d == "OOO":
                text_game_over = "GAME OVER\n  O WIN"
    else:
        text_game_over = "GAME OVER"

    return text_game_over


start_game()

while True:

    if open_logo:
        os.system("cls")
        print(
            "\n##############################\n#                            #\n#          GAME X O          #\n#                            #\n##############################\n"
        )
        print("Who will go first, X or O\n")
        print("1. Select X           1")
        print("2. Select O           2")
        print("3. Exit the game   exit\n")

    number_input = input("Select one item: ")

    if number_input == "1":
        open_logo = False
        select_X_O = "X"
    elif number_input == "2":
        open_logo = False
        select_X_O = "O"
    elif number_input == "exit":
        exit_game = True
    else:
        open_logo = False
        print("\nYou can't choose.\n")

    while select_X_O != "":

        os.system("cls")
        number_channel = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "exit"]
        open_channel = False

        print(show_X_O())
        print("\n" + select_X_O, "is a player.")
        print("Select a channel between 1 and 9.")
        print(text_error)
        text_error = ""
        number_input = input("Select a channel: ")

        for i in number_channel:
            if i == number_input:
                open_channel = True

        if open_channel:
            if number_input != "exit":

                number_input = int(number_input) - 1
                nub = 0

                for r in range(3):
                    for c in range(3):
                        if nub == number_input:

                            if table_X_O[r][c] == " ":
                                table_X_O[r][c] = select_X_O

                                if select_X_O == "X":
                                    select_X_O = "O"
                                else:
                                    select_X_O = "X"

                                text = check_X_O()

                                if text != "NO":
                                    os.system('cls')
                                    print(show_X_O())
                                    print("\n" + text + "\n")
                                    number_input = input("Press enter to start the game.: ")
                                    start_game()
                                    select_X_O = ""
                            else:
                                text_error = "\nThis channel has been selected.\n"

                        nub = nub + 1
            else:
                exit_game = True
                break
        else:
            text_error = "\nYou can't choose.\n"
    if exit_game:
        break
