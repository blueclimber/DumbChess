class GameBoard:
    def __init__(self):
        """
        set up a new game
        create the pieces objects with their colors and locations, passing in self as the board

        game data structure: 2D 8x8 list of piece objects or None

        have a list of kings to see if they are in check? or pieces?
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

    def move(self, from_coord, to_coord):
        """
        :param
        from_coord source Coordinate
        to_coord destination Coordinate
        Figure out which piece is in from_coord. If there is no piece there, immediately return False
        """
        start_row, start_col = from_coord
        end_row, end_col = to_coord
        piece = start_row,start_col
        if piece is None:
            print("no piece in the given coordinate")
            return False
        
        def within_Bounds():
            if(0<= end_row < 8 and 0<=end_col<8):
                return True
            else :
                False
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
