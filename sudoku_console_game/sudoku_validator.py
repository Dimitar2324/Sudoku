import constants


class SudokuValidator:

    @staticmethod
    def is_valid(position, num, board):

        def is_valid_column(_col, to_add):
            for i in range(0, constants.GRID_ROWS_COLS_COUNT):
                if board[i][_col] == to_add:
                    return False

            return True

        def is_valid_row(_row, to_add):
            for i in range(0, constants.GRID_ROWS_COLS_COUNT):
                if board[_row][i] == to_add:
                    return False

            return True

        def is_valid_box(_row, _col, to_add):

            row_lower_bound = _row // 3
            col_lower_bound = _col // 3

            for i in range(row_lower_bound * 3, (row_lower_bound + 1) * 3):
                for j in range(col_lower_bound * 3, (col_lower_bound + 1) * 3):
                    if board[i][j] == to_add:
                        return False

            return True

        row, col = position

        if is_valid_row(row, num) and is_valid_column(col, num) and is_valid_box(row, col, num):
            return True

        return False
