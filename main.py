from gameboard import *


def game_loop():
    """
    game driver
    create a new gameboard object Game
    loops through player turns, forcing valid moves and continuing until a king is taken
    returns the winning player
    """
    Game = GameBoard()
    print("""
    Welcome to dumb chess.
    White is uppercase, black is lowercase.
    Whoever takes their opponent's king wins!
    White goes first.
    Enter moves in the format 'A2-B2' meaning from-to""")

    Game.display()

    """
    make this all in a loop that switches the players back and forth
    """
    curr_player = "white"
    other_player = "black"

    while True:  # this will run unitl someone is in check, then it will return

        valid_move = False

        while not valid_move:
            move_from, move_to = get_move(curr_player)
            try:  # in a try except because we could be passing two None types into the move function - this can fail
                valid_move = move(Game, move_from, move_to, curr_player)
            except Exception as e:
                print(f"invalid move: {e}")
                valid_move = False

        Game.display()
        if Game.in_check(other_player):
            print(f"{other_player} in check")
        elif Game.in_check(curr_player):
            print(f"{curr_player} in check")

        if Game.over:
            return curr_player

        curr_player, other_player = other_player, curr_player


def get_move(player):
    """
    Take the user move input. Makes sure there is a hyphen.
    call convert_string_to_coordinate.
    return tuple of two coordinate objects
    """
    player_move = input(f"{player}'s turn, please enter a move: ")

    if "-" not in player_move:
        print(f"Invalid move, move must have a hyphen. Please use format 'A2-A3'")
        return None, None

    try:
        move_list = player_move.split('-')
    except:
        print(f"Invalid move, move must have a hyphen. Please use format 'A2-A3'")
        return None, None

    try:
        move_from = convert_string_to_coordinate(move_list[0])  # makes a coordinate object
        move_to = convert_string_to_coordinate(move_list[1])  # makes a coordinate object
    except Exception as e:
        print(f"Invalid move: {e}")

    return move_from, move_to


def convert_string_to_coordinate(coord):
    """
    take the input string and convert it into a coordinate object
    """
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row_col_list = list(coord)

    r = row_col_list[1]
    c = row_col_list[0]

    try:
        row = int(r) - 1
    except:
        print(f"invalid coordinate {coord} row, please use format A1")
        return

    try:
        col = c.lower()
    except:
        print(f"invalid coordinate {coord} column, please use format A1")
        return

    if not (0 <= row <= 7) or (col not in cols):
        print(f"invalid coordinate {coord}, please use format A1")
        return

    col = cols.index(col)

    new_coord = Coordinate(row, col)
    return new_coord


def move(game, from_coord, to_coord, player):
    """
    Call game.move
    return True if game.move succeeds, False otherwise
    """
    valid = game.move(from_coord, to_coord, player)

    return valid


def main():
    playing = True

    while playing:
        winner = game_loop()
        print(f"{winner} won!")

        again = input("Play again? y for yes, n for no: ")
        if again != 'y':
            playing = False


if __name__ == "__main__":
    main()
