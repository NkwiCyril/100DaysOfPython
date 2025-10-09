import random

game_board = """
    |    |    |    |
    ----------------
    |    |    |    |
    ----------------
    |    |    |    |
"""

game_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
positions = []


def update_game_board(symbol, position):
    """Updates the board with computer and user symbol"""

    if position and symbol:
        position_index = game_array.index(position)

        if position in game_array:
            game_array.insert(position_index, symbol)
            game_array.remove(position)

    return print(f"""
        |  {game_array[0]}  |  {game_array[1]}  |  {game_array[2]}  |
        -------------------
        |  {game_array[3]}  |  {game_array[4]}  |  {game_array[5]}  |
        -------------------
        |  {game_array[6]}  |  {game_array[7]}  |  {game_array[8]}  |
    """)


def check_if_occupied():
    """"""


def is_three_in_row(symbol, array):
    """Checks whether the player or computer have their symbols aligned"""

    if symbol == array[0] == array[1] == array[2] or symbol == array[3] == array[4] == array[5] or symbol == array[6] == array[7] == array[8] or symbol == array[0] == array[4] == array[8] or symbol == array[2] == array[4] == array[6] or symbol == array[0] == array[3] == array[6] or symbol == array[1] == array[4] == array[7] or symbol == array[2] == array[5] == array[8]:
        return True

    return False


def player_turn(player_symbol):

    print("Your Turn!")

    player_position = input("Pick a cell by letter: ").lower()

    if player_position not in game_array:
        print("Please pick a valid position")

    positions.append(player_position)

    update_game_board(player_symbol, player_position)

    result = is_three_in_row(player_symbol, game_array)

    return result


def computer_turn(computer_symbol):

    print("Computer's Turn!")

    computer_position = random.choice(game_array)

    print(f"COMPUTER POSITION: {computer_position}")

    positions.append(computer_position)

    update_game_board(computer_symbol, computer_position)

    result = is_three_in_row(computer_symbol, game_array)

    return result


print("Welcome to the game of Tic Tac Toe!\n")
print(game_board)

while True:

    # Clear both the game and positions array
    positions = []

    symbols = ["O", "X"]

    player_symbol = input(
        f"Pick your symbol, {symbols[0]} or {symbols[1]}: ").upper()

    if player_symbol not in symbols:
        print("Please pick a valid symbol")

        continue

    computer_symbol = "O" if player_symbol == "X" else "X"

    print(f"Your symbol: {player_symbol}")
    print(f"Computer symbol: {computer_symbol}\n")

    update_game_board("", "")

    players = ["c", "p"]

    print("Tossing coin...\n")

    starter = random.choice(players)

    print("Computer wins the coin toss" if starter ==
          "c" else "You win the coin toss")

    while True:  # len(positions) < 9

        print(f"POSITIONS OCCUPIED: {positions}")

        if starter == "c":
            computer_result = computer_turn(computer_symbol)

            if computer_result:
                print("COMPUTER WINS!")

                break

            player_result = player_turn(player_symbol)

            if player_result:
                print("YOU WIN!")

        else:

            player_result = player_turn(player_symbol)
            if player_result:
                print("YOU WIN!")

                break

            computer_result = computer_turn(computer_symbol)
            if computer_result:
                print("COMPUTER WINS!")

                break

    break
