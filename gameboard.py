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

    def setup_pieces(self):
        # Place pawns
        for col in range(8):
            self.board[1][col] = Pawn(Coordinate(1, col), "black", self)
            self.board[6][col] = Pawn(Coordinate(6, col), "white", self)

        # Place rooks
        self.board[0][0] = self.board[0][7] = Rook(Coordinate(0, 0), "black", self)
        self.board[7][0] = self.board[7][7] = Rook(Coordinate(7, 0), "white", self)

        # Place knights
        self.board[0][1] = self.board[0][6] = Knight(Coordinate(0, 1), "black", self)
        self.board[7][1] = self.board[7][6] = Knight(Coordinate(7, 1), "white", self)

        # Place bishops
        self.board[0][2] = self.board[0][5] = Bishop(Coordinate(0, 2), "black", self)
        self.board[7][2] = self.board[7][5] = Bishop(Coordinate(7, 2), "white", self)

        # Place queens
        self.board[0][3] = Queen(Coordinate(0, 3), "black", self)
        self.board[7][3] = Queen(Coordinate(7, 3), "white", self)

        # Place kings
        self.board[0][4] = King(Coordinate(0, 4), "black", self)
        self.board[7][4] = King(Coordinate(7, 4), "white", self)

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
        print("  A   B   C   D   E   F   G   H")
        print("  ---------------------------------")
        for row in range(8):
            row_str = f"{8 - row} |"
            for col in range(8):
                piece = self.board[row][col]
                row_str += f" {piece.__class__.__name__[0] if piece else ' '} |"
            print(row_str)
            print("  ---------------------------------")

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

        if not (0 <= to_coord.row < 8 and 0 <= to_coord.col < 8):
            return False    # return False, not true because if this happens it's invalid
        # else:
        #     False     no elses - makes anything following unreachable.

        valid = piece.move(to_coord)    # now call the piece's move function.

        if valid:
            self.board[from_coord.row][from_coord.column] = None
            self.board[to_coord.row][to_coord.column] = piece
        return valid
        """        
        def is_piece_w_B():
        if the piece is used as tupple("piece Name", "color","coordinate","firstTime")
        pieceColor = piece[1] which would give the color
        if pieceColor is black || white:
            
            return True;
        else 
             return Fale;
        
        """

        """
        Decide if that piece can legally be moved by the currant player - is the current player white
            and the piece belongs to black?
            if it's illegal immediately return False
        Then call that pieces move function. That will check if the movement fits in that pieces rules and return a bool
        :return: True if valid move and carried out, False otherwise
        """

    def in_check(self, color):
        """
        check to see if the king is in check.
        How do we know which king is in check? How do we find the two king's positions? hmmm, solve this one we must
        return True if in check
        return false otherwise
        """


class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
