import constants
from sudoku_validator import SudokuValidator


class SudokuSolver:

    @staticmethod
    def solve(board):

        def find_empty_cell():
            for k in range(constants.GRID_ROWS_COLS_COUNT):
                for j in range(constants.GRID_ROWS_COLS_COUNT):
                    if board[k][j] == 0:
                        return k, j

            return None

        pos = find_empty_cell()

        if pos is None:
            return True

        current_row, current_col = pos

        for i in range(1, constants.GRID_ROWS_COLS_COUNT + 1):
            if SudokuValidator.is_valid(pos, i, board):
                board[current_row][current_col] = i

                if SudokuSolver.solve(board):
                    return True

                board[current_row][current_col] = 0

        return False
