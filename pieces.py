from abc import ABC


class Piece:
    def __init__(self, position, color, board):
        self.position = position
        self.color = color
        self.board = board

    def move(self, new_position):
        """
        :param
        new_position - a new boardgame position

        if new_position is valid, set self.position = new_position
        remember to check for pieces that are in between current position and new position. That makes the
        move invalid for everyone except the knight

        If there is a piece taken, find it on self.board and remove it?
        :return
        bool True if valid position and position changed, False otherwise
        """
        pass

    # maybe add another method is_valid

class King(Piece):
    def move(self, new_position):
        pass

class Queen(Piece):
    def move(self, new_position):
        pass

class Knight(Piece):
    def move(self, new_position):
        pass

class Bishop(Piece):
    def move(self, new_position):
        pass

class Rook(Piece):
    def move(self, new_position):
        pass

class Pawn(Piece):
    def move(self, new_position):
        pass
