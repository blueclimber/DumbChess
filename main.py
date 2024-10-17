def game_loop():
    """
    create a new gameboard object Game
    set player turn to black or white
    while not in check? or while get move != q or something like that...
    alternate player between white and black
    get_move(player)
    Game.move
    """
    pass


def get_move(player):
    valid = False
    move = input(f"{player}'s turn: Please enter a move")

    """
    check move for validity
    while not valid:
        prompt for another move
    return move
    """
    pass


def main():
    game_loop()


if __name__ == "__main__":
    main()

