from pieces import King, Queen, Knight, Bishop, Rook, Pawn


class GameBoard:
    def __init__(self):
        self.board = []
        """
        set up a new game
        create the pieces objects with their colors and locations, passing in self as the board

        game data structure: 2D 8x8 list of piece objects or None

        have a list of kings to see if they are in check? or pieces?
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

        self.kings = {"white": Coordinate(7, 4), "black": Coordinate(0, 4)}

    def setup_pieces(self):
        # Place pawns
        for col in range(8):
            self.board[1][col] = Pawn(Coordinate(1, col), "white", self, "pawn")
            self.board[6][col] = Pawn(Coordinate(6, col), "black", self, "pawn")

        # Place rooks
        self.board[0][0] = Rook(Coordinate(0, 0), "white", self, "rook")
        self.board[0][7] = Rook(Coordinate(0, 7), "white", self, "rook")
        self.board[7][0] = Rook(Coordinate(7, 0), "black", self, "rook")
        self.board[7][7] = Rook(Coordinate(7, 7), "black", self, "rook")

        # Place knights
        self.board[0][1] = Knight(Coordinate(0, 1), "white", self, "knight")
        self.board[0][6] = Knight(Coordinate(0, 6), "white", self, "knight")
        self.board[7][1] = Knight(Coordinate(7, 1), "black", self, "knight")
        self.board[7][6] = Knight(Coordinate(7, 6), "black", self, "knight")

        # Place bishops
        self.board[0][2] = Bishop(Coordinate(0, 2), "white", self, "bishop")
        self.board[0][5] = Bishop(Coordinate(0, 5), "white", self, "bishop")
        self.board[7][2] = Bishop(Coordinate(7, 2), "black", self, "bishop")
        self.board[7][5] = Bishop(Coordinate(7, 5), "black", self, "bishop")

        # Place queens
        self.board[0][3] = Queen(Coordinate(0, 3), "white", self, "queen")
        self.board[7][3] = Queen(Coordinate(7, 3), "black", self, "queen")

        # Place kings
        self.board[0][4] = King(Coordinate(0, 4), "white", self, "king")
        self.board[7][4] = King(Coordinate(7, 4), "black", self, "king")

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
        print()
        print("    A   B   C   D   E   F   G   H")
        print("  ---------------------------------")
        for row in range(7, -1, -1):
            row_str = f"{row + 1} |"
            for col in range(8):
                piece = self.board[row][col]

                if piece and piece.color == "white":
                    if piece.name == "knight":
                        row_str += f" N |"
                    else:
                        row_str += f" {piece.__class__.__name__[0] if piece else ' '} |"
                else:
                    if piece and piece.name == "knight":
                        row_str += f" n |"
                    else:
                        row_str += f" {piece.__class__.__name__[0].lower() if piece else ' '} |"
            print(row_str)
            print("  ---------------------------------")
        print()

    def move(self, from_coord, to_coord, color):
        """
        :param
        from_coord source Coordinate
        to_coord destination Coordinate
        Figure out which piece is in from_coord. If there is no piece there, immediately return False
        """
        piece = self.board[from_coord.row][from_coord.column]
        if piece is None:
            print("No piece in the coordinate")
            return False
        if piece.color != color:
            print(f"You are trying to move the {piece.color}'s piece.")
            return False
        # else:
        #     return True   This makes the rest of the code unreachable

        to_piece = self.board[to_coord.row][to_coord.column]
        if to_piece and to_piece.color == color:
            print("You can't take yourself")
            return False

        if not (0 <= to_coord.row < 8 and 0 <= to_coord.column < 8):
            print("you are trying to move off of the gameboard")
            return False    # return False, not true because if this happens it's invalid

        # else:
        #     False     no elses - makes anything following unreachable.

        valid = piece.move(to_coord)    # now call the piece's move function.

        if valid:
            self.board[from_coord.row][from_coord.column] = None
            self.board[to_coord.row][to_coord.column] = piece
            piece.position = to_coord

            if piece.name == "pawn":
                if color == "white":
                    if to_coord.row == 7:
                        self.board[to_coord.row][to_coord.column] = Queen(to_coord, "white", self, "queen")
                else:
                    if to_coord.row == 0:
                        self.board[to_coord.row][to_coord.column] = Queen(to_coord, "black", self, "queen")

        return valid


    def in_check(self, color):
        """
        check to see if the king is in check.
        return True if in check
        return false otherwise
        """
        # Get the position of the king for the given color
        king_position = self.kings[color]

        # Iterate over the entire board to check for threats to the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                # Check if the piece is an enemy and can move to the king's position
                if piece and piece.color == color:
                    if piece.check_for_check(king_position):
                        return True  # The king is in check

        return False  # The king is not in check


class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
