import random
import Constants
import Exceptions
from SudokuSolver import Solver
from SudokuGenerator import Generator
from DrawingManager import Drawer
from copy import deepcopy
from InputValidator import IValidator


class Grid:

    def __init__(self, level_of_difficulty, sudoku_type):
        self.sudoku = Generator.generate_random(level_of_difficulty) if sudoku_type == 'random' \
            else Generator.generate_from_personals(level_of_difficulty)
        self.solved_sudoku = deepcopy(self.sudoku)
        Solver.solve(self.solved_sudoku)
        self.hints_allowed = Constants.ALLOWED_HINTS_PER_GAME
        self.mistakes_allowed = Constants.ALLOWED_MISTAKES_PER_GAME
        self.unofficial_moves = {}

    def give_hint(self):

        row = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)
        col = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)

        while self.sudoku[row][col] != 0:
            row = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)
            col = random.randint(0, Constants.GRID_ROWS_COLS_COUNT - 1)

        self.sudoku[row][col] = self.solved_sudoku[row][col]
        if (row, col) in self.unofficial_moves.keys():
            self.unofficial_moves.pop((row, col))

    def is_solved(self):

        for i in range(Constants.GRID_ROWS_COLS_COUNT):
            for j in range(Constants.GRID_ROWS_COLS_COUNT):
                if self.sudoku[i][j] != self.solved_sudoku[i][j]:
                    return False

        return True

    def start(self):
        while self.mistakes_allowed > 0 and not self.is_solved():
            try:
                Drawer.draw_grid(self.sudoku, self.unofficial_moves)

                current_move = input('Enter position - (row, col) or number 10 for hint: ')

                if current_move == Constants.HINT_WANTED:

                    IValidator.check_hints_available(self.hints_allowed)

                    self.give_hint()
                    self.hints_allowed -= 1
                    continue

                args = current_move.split()
                IValidator.is_invalid_tuple(args)
                IValidator.check_arguments_of_tuple(args)

                position = tuple(int(item) - 1 for item in args)
                IValidator.is_invalid_pos(position, 0, Constants.GRID_ROWS_COLS_COUNT)
                IValidator.is_filled_pos(self.sudoku, position)

                str_num = input('Enter your num: ')
                IValidator.is_invalid_input_type(str_num)
                current_candidate = int(str_num)
                IValidator.is_invalid_num(current_candidate, 1, Constants.GRID_ROWS_COLS_COUNT + 1)

                confirmation = input('With pencil: ')
                IValidator.is_invalid_confirmation(confirmation)

                if confirmation == 'no':
                    if self.solved_sudoku[position[0]][position[1]] == current_candidate:
                        self.sudoku[position[0]][position[1]] = current_candidate

                        if position in self.unofficial_moves.keys():
                            self.unofficial_moves.pop(position)
                    else:
                        self.mistakes_allowed -= 1
                        if position in self.unofficial_moves.keys():
                            self.unofficial_moves.pop(position)

                        raise Exceptions.WrongMoveException()
                elif confirmation == 'yes':
                    self.unofficial_moves[position] = current_candidate
            except Exception as er:
                print(er)

        if self.mistakes_allowed == 0:
            print(Constants.LOSING_MESSAGE)
            self.unofficial_moves.clear()
            Drawer.draw_grid(self.solved_sudoku, self.unofficial_moves)
        else:
            print(Constants.WINNING_MESSAGE)
