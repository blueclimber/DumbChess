import unittest
from gameboard import GameBoard
from pieces import King, Queen, Rook, Bishop, Knight, Pawn, Coordinate
from main import move, convert_string_to_coordinate

class TestChessGame(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()

    def test_initial_board_setup(self):
        # Check that each piece is in the correct initial position
        self.assertIsInstance(self.board.board[0][0], Rook)  # White rook
        self.assertIsInstance(self.board.board[7][4], King)  # Black king
        self.assertIsInstance(self.board.board[1][0], Pawn)  # White pawn
        self.assertIsNone(self.board.board[3][3])            # Empty square

    def test_move_pawn(self):
        # Move white pawn from E2 to E4
        start = convert_string_to_coordinate("E2")
        end = convert_string_to_coordinate("E4")
        result = move(self.board, start, end, "white")
        self.assertTrue(result)
        self.assertIsInstance(self.board.board[3][4], Pawn)
        self.assertIsNone(self.board.board[1][4])

    def test_invalid_move(self):
        # Attempt to move pawn backward, which should fail
        start = convert_string_to_coordinate("E2")
        end = convert_string_to_coordinate("E1")
        result = move(self.board, start, end, "white")
        self.assertFalse(result)

    def test_capture(self):
        # Set up a scenario to capture a piece
        result1 = move(self.board, convert_string_to_coordinate("E2"), convert_string_to_coordinate("E4"), "white")
        self.assertTrue(result1)
        result2 = move(self.board, convert_string_to_coordinate("D7"), convert_string_to_coordinate("D5"), "black")
        self.assertTrue(result2)
        result3 = move(self.board, convert_string_to_coordinate("E4"), convert_string_to_coordinate("D5"), "white")
        self.assertTrue(result3)  # Capture should succeed
        self.assertIsInstance(self.board.board[4][3], Pawn)  # White pawn in new position
        self.assertIsNone(self.board.board[6][3])            # Black pawn is captured

    def test_check_detection(self):
        # Set up check on black king
        move(self.board, convert_string_to_coordinate("E2"), convert_string_to_coordinate("E4"), "white")
        move(self.board, convert_string_to_coordinate("F7"), convert_string_to_coordinate("F6"), "black")
        move(self.board, convert_string_to_coordinate("D1"), convert_string_to_coordinate("H5"), "white")
        self.assertTrue(self.board.in_check("black"))

    def test_endgame_king_capture(self):
        # Capture black king to end game
        moves = [
            ("E2", "E4"), ("E7", "E5"),
            ("D1", "H5"), ("B8", "C6"),
            ("H5", "E8")  # Queen captures black king
        ]
        for move_from, move_to in moves:
            start = convert_string_to_coordinate(move_from)
            end = convert_string_to_coordinate(move_to)
            result = move(self.board, start, end, "white" if move_from[1] == '2' else "black")
        self.assertTrue(self.board.in_check("black"))

    def test_pawn_promotion(self):
        # Promote a white pawn
        print(f"TEST_PAWN_PROMOTION, Piece at [6][0]: {self.board.board[6][0]}")
        print(f"TEST_PAWN_PROMOTION, Piece at [7][0]: {self.board.board[7][0]}")
        self.board.board[6][1] = Pawn(Coordinate(6, 1), "white", self.board, "pawn")
        print(f"TEST_PAWN_PROMOTION, Piece at [6][0]: {self.board.board[6][0]}")
        move(self.board, Coordinate(6, 1), Coordinate(7, 0), "white")
        print(f"TEST_PAWN_PROMOTION, Piece at [7][0]: {self.board.board[7][0]}")
        self.assertTrue(self.board.board[7][0], Queen)  # Pawn should promote to queen

    def test_knight_move(self):
        # Test knight movement
        start = convert_string_to_coordinate("B1")
        end = convert_string_to_coordinate("C3")
        result = move(self.board, start, end, "white")
        self.assertTrue(result)
        self.assertIsInstance(self.board.board[2][2], Knight)

    def test_blocked_path(self):
        # Attempt to move queen through a pawn
        start = convert_string_to_coordinate("D1")
        end = convert_string_to_coordinate("D3")
        result = move(self.board, start, end, "white")
        self.assertFalse(result)  # Move should be invalid as path is blocked

if __name__ == '__main__':
    unittest.main()
