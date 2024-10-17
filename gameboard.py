class GameBoard:
    def __init__(self):
        """
        set up a new game
        create the pieces objects with their colors and locations

        game data structure: 2D 8x8 list of piece objects or None
        """
        pass

    def display(self):
        """
        how to display the game
        Display:
        You need an 8x8 board. The easiest thing to program, and probably to visualize is a grid of boxes formed by
        vertical and horizontal lines. (“|” and “-“)
        You need some way of labeling the pieces. I recommend the following for display: k,q,b,n,r,p for the black
        pieces, and the same letters upper case for white.  Note that the knight is “n”. If you choose a different
        representation, let the tester know.
        The board is labeled as follows: From where WHITE sits, the ranks (rows) are labeled 1 through 8 (bottom to
        top). The files (columns) are labeled A through H (left to right).
        For example, the white has rooks (castles) on A1 and H1, and the white king is on E1. The black king is on E8.
        It would be nice to have the labels on the board you display, but you decide.
        If you choose a different labeling scheme, make sure the tester knows.

        """

    def move(self, command):
        """
        5.	Commands are “source – destination”, or something similar, using the coordinates as follows: “E2 – E4”.
        Decide on whether you want spaces, and whether you want upper or lower case letters, etc.
        :param command: source-destination
        :return: True if valid move and carried out, False otherwise
        """
