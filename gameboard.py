from pieces import King, Queen, Knight, Bishop, Rook, Pawn, Coordinate


class GameBoard:
    def __init__(self):
        self.board = []
        """
        set up a new game
        create the pieces objects with their colors and locations, passing in self as the board
        game.board structure: 2D 8x8 list of piece objects or None
        self.kings is a dictionary of king color and location, used for checking if king is in check
        self.over is a placeholder that gets change to True if a king is captured
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.kings = {"white": Coordinate(7, 4), "black": Coordinate(0, 4)}
        self.over = False

    def setup_pieces(self):
        """
        create each piece and place in it's starting location
        no return
        """
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
        prints the game
        no return
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

    # def move(self, from_coord, to_coord, color):
    #     """
    #     :param
    #     from_coord source Coordinate
    #     to_coord destination Coordinate
    #     Figure out which piece is in from_coord. If there is no piece there, immediately return False
    #     Check that the piece's color matches the current player
    #     Checks to_coord. If a piece is there makes sure it is the opponant's color
    #     Ensures that player is moving to a real location on the board
    #     Call's the pieces move function, and stores the return value in valid
    #     If the move is valid, check if the piece is a pawn, and if it is, and is at the last row, promote it to a queen
    #     If the move is valid, and there is a piece in the to_coord, if it's a king report the win, otherwise report
    #     on the capture
    #     Return valid
    #     """
    #     piece = self.board[from_coord.row][from_coord.column]
    #     if piece is None:
    #         print("No piece in the coordinate")
    #         return False
    #     if piece.color != color:
    #         print(f"You are trying to move the {piece.color}'s piece.")
    #         return False

    #     to_piece = self.board[to_coord.row][to_coord.column]
    #     if to_piece and to_piece.color == color:
    #         print("You can't take yourself")
    #         return False

    #     if not (0 <= to_coord.row < 8 and 0 <= to_coord.column < 8):
    #         print("you are trying to move off of the gameboard")
    #         return False

    #     valid = piece.move(to_coord)    # now call the piece's move function.

    #     if piece.name == "pawn":
    #         # Handle diagonal capture
    #         if abs(from_coord.column - to_coord.column) == 1 and \
    #         ((color == "white" and to_coord.row == from_coord.row + 1) or 
    #             (color == "black" and to_coord.row == from_coord.row - 1)):
    #             if to_piece and to_piece.color != color:
    #                 valid = True
    #         # Handle standard forward move for pawns
    #         elif from_coord.column == to_coord.column and to_piece is None:
    #             valid = piece.move(to_coord)
    #         else:
    #             valid = False

    #     if valid:
    #         self.board[from_coord.row][from_coord.column] = None
    #         self.board[to_coord.row][to_coord.column] = piece
    #         piece.position = to_coord

    #         if piece.name == "pawn":
    #             if color == "white":
    #                 if to_coord.row == 7:
    #                     print(f"Promoting {color} Pawn to Queen")
    #                     self.board[to_coord.row][to_coord.column] = Queen(to_coord, "white", self, "queen")
    #             else:
    #                 if to_coord.row == 0:
    #                     print(f"Promoting {color} Pawn to Queen")
    #                     self.board[to_coord.row][to_coord.column] = Queen(to_coord, "black", self, "queen")

    #         if to_piece and to_piece.name == "king":
    #             self.over = True
    #         elif to_piece:
    #             print(f"{to_piece.color} {to_piece.name} captured")

    #     return valid

    def move(self, from_coord, to_coord, color):
        piece = self.board[from_coord.row][from_coord.column]
        if piece is None:
            print("No piece in the coordinate")
            return False

        if piece.color != color:
            print(f"You are trying to move the {piece.color}'s piece.")
            return False

        to_piece = self.board[to_coord.row][to_coord.column]
        if to_piece and to_piece.color == color:
            print("You can't take yourself")
            return False
        
        if not (0 <= to_coord.row < 8 and 0 <= to_coord.column < 8):
            print("you are trying to move off of the gameboard")
            return False

        print(f"Attempting to move {color} {piece.name} from ({from_coord.row},{from_coord.column}) to ({to_coord.row},{to_coord.column})")

        valid = piece.move(to_coord)

        # Special handling for pawns (including diagonal captures and promotion)
        if piece.name == "pawn":
            # Handle diagonal capture
            if abs(from_coord.column - to_coord.column) == 1 and \
            ((color == "white" and to_coord.row == from_coord.row + 1) or 
                (color == "black" and to_coord.row == from_coord.row - 1)):
                if to_piece and to_piece.color != color:
                    valid = True
            # Handle standard forward move for pawns
            elif from_coord.column == to_coord.column and to_piece is None:
                valid = piece.move(to_coord)
            else:
                valid = False

        if valid:
            # Move the piece on the board
            self.board[from_coord.row][from_coord.column] = None
            self.board[to_coord.row][to_coord.column] = piece
            piece.position = to_coord

            # Update the king's position if the king moved
            if piece.name == "king":
                self.kings[color] = to_coord

            # Promotion for pawns reaching the last rank
            if piece.name == "pawn" and ((piece.color == "white" and to_coord.row == 7) or (color == "black" and to_coord.row == 0)):
                print(f"Promoting {color} Pawn to Queen at {to_coord}")
                # Replace the pawn with a queen in the `to_coord` position
                self.board[to_coord.row][to_coord.column] = Queen(to_coord, color, self, "queen")
                # Debugging: Check the promotion status
                print(f"Promotion complete: {self.board[to_coord.row][to_coord.column]}")

            # Handle capture announcement
            if to_piece:
                if to_piece.name == "king":
                    self.over = True
                    print(f"{color} wins! Captured the king.")
                else:
                    print(f"{color} captured {to_piece.color} {to_piece.name}")

        return valid

        


    # def in_check(self, color):
    #     """
    #     check to see if the king is in check.
    #     return True if in check
    #     return false otherwise
    #     """
    #     # Get the position of the king for the given color
    #     king_position = self.kings[color]

    #     # Iterate over the entire board to check for threats to the king
    #     for row in range(8):
    #         for col in range(8):
    #             piece = self.board[row][col]
    #             # Check if the piece is an enemy and can move to the king's position
    #             if piece and piece.color == color:
    #                 if piece.check_for_check(king_position):
    #                     return True  # The king is in check

    #     return False  # The king is not in check
    def in_check(self, color):
        """
        Check if the king of the specified color is in check.
        """
        king_position = self.kings[color]  # Get the position of the king for the given color

        # Iterate over the board to check for enemy pieces that can attack the king's position
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                # Check if the piece belongs to the opponent and can move to the king's position
                if piece and piece.color != color:
                    if piece.check_for_check(king_position):
                        print(f"{color} king is in check by {piece.color} {piece.name} at {piece.position}")
                    return True  # The king is in check

        return False  # The king is not in check


# class Coordinate:
#     def __init__(self, row, column):
#         self.row = row
#         self.column = column
