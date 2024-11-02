from abc import ABC, abstractmethod


class Piece:
    def __init__(self, position, color, board, name):
        self.name = name
        self.position = position
        self.color = color
        self.board = board  # this is a GameBoard object, so when these pieces are created, GameBoard will pass in self

    @abstractmethod
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

    @abstractmethod
    def check_for_check(self, new_position):
        pass
    def is_enemy(self, other):
        """Check if another piece is an enemy (opposite color)."""
        return other and self.color != other.color
    def is_within_bounds(self, position):
        """Check if a position is within the board bounds."""
        return 0 <= position.row < 8 and 0 <= position.column < 8
    def path_clear(self, start, end):
        """Check if the path is clear between two coordinates (exclusive)."""
        row_step = 1 if end.row > start.row else -1 if end.row < start.row else 0
        col_step = 1 if end.column > start.column else -1 if end.column < start.column else 0
        current = Coordinate(start.row + row_step, start.column + col_step)

        while current.row != end.row or current.column != end.column:
            if self.board.board[current.row][current.column] is not None:
                return False
            current = Coordinate(current.row + row_step, current.column + col_step)
        return True

    # maybe add another method is_valid


class King(Piece):
    def move(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if row_diff > 1 or col_diff > 1:
            print("Kings can only move one space")
            return False  # Kings can move one square in any direction
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        return True

        # if row_diff <= 1 and col_diff <= 1 and self.is_within_bounds(new_position):
        #     return True  # Kings can move one square in any direction
        # return False

    def check_for_check(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if row_diff <= 1 and col_diff <= 1 and self.is_within_bounds(new_position):
            return True  # Kings can move one square in any direction
        return False


class Queen(Piece):
    def move(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if not(row_diff == col_diff or row_diff == 0 or col_diff == 0):
            print("Queens must move in a straight or diagonal line")
            return False
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        elif not self.path_clear(self.position, new_position):
            print("Queens cannot jump over other players")
            return False
        return True

    def check_for_check(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if (row_diff == col_diff or row_diff == 0 or col_diff == 0) and self.is_within_bounds(new_position) and self.path_clear(self.position, new_position):
            return True
        return False


class Knight(Piece):
    def move(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if (row_diff, col_diff) not in [(2, 1), (1, 2)]:
            print("Knights must move down two and over one or down one and over two")
            return False
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        return True

    def check_for_check(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if (row_diff, col_diff) in [(2, 1), (1, 2)] and self.is_within_bounds(new_position):
            return True
        return False


class Bishop(Piece):
    def move(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if row_diff != col_diff:
            print("Bishops must move in a diagonal line")
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        elif not self.path_clear(self.position, new_position):
            print("Bishops cannot jump over other players")
            return False
        return True

    def check_for_check(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if row_diff == col_diff and self.is_within_bounds(new_position) and self.path_clear(self.position, new_position):
            return True
        return False


class Rook(Piece):
    def move(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if not(row_diff == 0 or col_diff == 0):
            print("Rooks must move in a straight line")
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        elif not self.path_clear(self.position, new_position):
            print("Rooks cannot jump over other players")
            return False
        return True

    def check_for_check(self, new_position):
        row_diff = abs(self.position.row - new_position.row)
        col_diff = abs(self.position.column - new_position.column)
        if (row_diff == 0 or col_diff == 0) and self.is_within_bounds(new_position) and self.path_clear(self.position, new_position):
            return True
        return False


class Pawn(Piece):
    def move(self, new_position):
        row_diff = new_position.row - self.position.row
        col_diff = new_position.column - self.position.column

        if self.color == 'white':
            forward = 1
            start_row = 1
        else:
            forward = -1
            start_row = 6

        if col_diff != 0:
            print("Pawns can only move forward")
            return False
        elif row_diff >= 2 and self.position.row != start_row:
            print("Pawns must move only one space except from the start position")
            return False
        if row_diff > 2:
            print("Pawns may only move one or two spaces from the start position")
            return False
        elif not self.is_within_bounds(new_position):
            print("You are trying to move off the board")
            return False
        elif not self.path_clear(self.position, new_position):
            print("Pawns cannot jump over other players")
            return False

        return True



    def check_for_check(self, new_position):
        row_diff = new_position.row - self.position.row
        col_diff = new_position.column - self.position.column

        if self.color == 'white':
            forward = 1
            start_row = 1
        else:
            forward = -1
            start_row = 6

        if col_diff == 0 and row_diff == forward and not self.board.board[new_position.row][new_position.column]:
            return True
        if col_diff == 0 and row_diff == 2 * forward and self.position.row == start_row and not self.board.board[self.position.row + forward][self.position.column] and not self.board.board[new_position.row][new_position.column]:
            return True
        if col_diff == 1 and row_diff == forward and self.is_enemy(self.board.board[new_position.row][new_position.column]):
            return True
        return False

class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
