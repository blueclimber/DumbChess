from gameboard import *


def game_loop():
    """
    create a new gameboard object Game
    set player turn to black or white
    while not in check? or while get move != q or something like that...
    alternate player between white and black

    """
    Game = GameBoard()
    Game.display()

    """
    make this all in a loop that switches the players back and forth
    """
    curr_player = "white"
    other_player = "black"

    while True: # this will run unitl someone is in check, then it will return


        valid_move = False

        while not valid_move:
            move_from, move_to = get_move(curr_player)
            try:    # in a try except because we could be passing two None types into the move function - this can fail
                valid_move = move(Game, move_from, move_to, curr_player)
            except Exception as e:
                print(f"invalid move: {e}")
                valid_move = False

        Game.display()
        if Game.in_check(other_player):
            return curr_player
        elif Game.in_check(curr_player):
            return other_player

        curr_player, other_player = other_player, curr_player


def get_move(player):
    """
    move needs to be from-two
    example E4-D3

    convert input string to two sets of indices using convert_coord_to_index, and then convert to coordinates for
        easy use
    """
    player_move = input(f"{player}'s turn: Please enter a move: ")
    move_list = player_move.split('-')

    move_from = convert_string_to_coordinate(move_list[0])  # makes a coordinate object
    move_to = convert_string_to_coordinate(move_list[1])    # makes a coordinate object

    return move_from, move_to


def convert_string_to_coordinate(coord):
    """
    take the input string and convert it into two indices
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

    if not(0 <= row <= 7) or (col not in cols):
        print(f"invalid coordinate {coord}, please use format A1")
        return

    col = cols.index(col)

    new_coord = Coordinate(row, col)
    return new_coord


def move(game, from_coord, to_coord, player):
    """
    This actually calls the Game.move()
    Game.move() returns a bool, this returns that same bool
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
