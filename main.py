from gameboard import *


def game_loop():
    """
    create a new gameboard object Game
    set player turn to black or white
    while not in check? or while get move != q or something like that...
    alternate player between white and black

    """
    Game = GameBoard()

    """
    make this all in a loop that switches the players back and forth
    """
    curr_player = "white"

    Game.display()

    valid_move = False

    while not valid_move:
        f, t = get_move(curr_player)
        valid_move = move(Game, f, t, curr_player)
    pass

    # change to check for each player
    # if Game.in_check():
    #     print("some player is currently in check")
    #     pass
    #     # end the game?

    """
    end loop
    """


def get_move(player):
    """
    move needs to be from-two
    example E4-D3

    convert input string to two sets of indices using convert_coord_to_index, and then convert to coordinates for
        easy use
    """
    valid = False
    player_move = input(f"{player}'s turn: Please enter a move")

    move_list = player_move.split('-')

    move_from = convert_string_to_coordinate(move_list[0])  # makes a coordinate object

    move_to = convert_string_to_coordinate(move_list[1])    # makes a coordinate object

    """

    check move for validity - is the format correct, do the spaces exist
    while not valid:
        prompt for another move
    return move_from, move_to
    """
    return move_from, move_to


def convert_string_to_coordinate(coord):
    """
    take the input string and convert it into two indices
    """
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    row_col_list = coord.split('')

    row = int(row_col_list[0]) - 1
    # fixme - what if column is lowercase, or not in the cols list
    col = cols.index(row_col_list[1]) - 1

    new_coord = Coordinate(row, col)
    return new_coord


def move(game, from_coord, to_coord, player):
    """
    This actually calls the Game.move()
    Game.move() returns a bool, this returns that same bool
    """
    game.move()

    return True


def main():
    game_loop()


if __name__ == "__main__":
    main()
