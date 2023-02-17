import linecache
import math
import random
import Constants
from SudokuSolver import Solver


class Generator:

    @staticmethod
    def generate_from_personals(difficulty_level):
        file_name = difficulty_level + ".txt"

        with open(file_name) as f:
            lines_count = len(f.readlines())

        line = random.randint(1, lines_count)
        current_sudoku = linecache.getline(file_name, line)

        row = 0
        col = 0
        grid = [[0 for x in range(Constants.GRID_ROWS_COLS_COUNT)] for y in range(Constants.GRID_ROWS_COLS_COUNT)]

        for i in range(0, len(current_sudoku) - 1):
            if i % Constants.GRID_ROWS_COLS_COUNT == 0 and i != 0:
                col = 0
                row += 1

            grid[row][col] = int(current_sudoku[i])
            col += 1

        return grid

    @staticmethod
    def generate_random(difficulty_level):

        def used_in_box(row, col, num, board, step):
            for i in range(step):
                for j in range(step):
                    if board[row + i][col + j] == num:
                        return True
            return False

        def fill_box(board, row, col, step):

            value = 0
            for i in range(step):
                for j in range(step):
                    while True:
                        value = random.randint(1, Constants.GRID_ROWS_COLS_COUNT)
                        if not used_in_box(row, col, value, board, step):
                            break

                    board[row + i][col + j] = value

        def fill_diagonal_boxes(board):

            step = int(math.sqrt(Constants.GRID_ROWS_COLS_COUNT))
            for i in range(0, Constants.GRID_ROWS_COLS_COUNT, step):
                fill_box(board, i, i, step)

        def remove_cells(cells_count, board):

            while cells_count != 0:
                row = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)
                col = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)

                if board[row][col] != 0:
                    cells_count -= 1
                    board[row][col] = 0

        grid = [[0 for x in range(Constants.GRID_ROWS_COLS_COUNT)] for y in range(Constants.GRID_ROWS_COLS_COUNT)]

        digits_to_remove = 0
        if difficulty_level == 'easy':
            digits_to_remove = Constants.EASY_LEVEL_REMOVED_DIGITS_COUNT
        elif difficulty_level == 'medium':
            digits_to_remove = Constants.MEDIUM_LEVEL_REMOVED_DIGITS_COUNT
        else:
            digits_to_remove = Constants.HARD_LEVEL_REMOVED_DIGITS_COUNT

        fill_diagonal_boxes(grid)
        Solver.solve(grid)
        remove_cells(digits_to_remove, grid)

        return grid
