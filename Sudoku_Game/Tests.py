import unittest
import numpy
import Constants
import Exceptions
from SudokuValidator import Validator
from SudokuSolver import Solver
from SudokuGenerator import Generator
from Board import Grid
from Engine import Engine
from InputValidator import IValidator


class TestSudokuValidator(unittest.TestCase):
    def test_for_invalid_addition_in_row(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        result = Validator.is_valid((0, 2), 7, sudoku)
        self.assertEqual(result, False)

    def test_for_invalid_addition_in_col(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        result = Validator.is_valid((2, 0), 7, sudoku)
        self.assertEqual(result, False)

    def test_for_invalid_addition_in_3x3_box(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        result = Validator.is_valid((0, 2), 8, sudoku)
        self.assertEqual(result, False)

    def test_for_valid_move(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        result = Validator.is_valid((2, 0), 1, sudoku)
        self.assertEqual(result, True)


class TestSudokuSolver(unittest.TestCase):

    def test_whether_solving_right(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        solved = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

        Solver.solve(sudoku)
        result = numpy.array_equiv(solved, sudoku)
        self.assertEqual(result, True)


class TestSudokuGenerator(unittest.TestCase):

    def test_for_generating_easy_sudoku_from_right_file(self):

        sudoku = ''.join([str(i) for i in (numpy.array(Generator.generate_from_personals('easy')) .flatten())])
        with open('easy.txt') as f:
            lines = f.readlines()

        self.assertTrue(lines.count(sudoku + "\n") > 0)

    def test_for_generating_medium_sudoku_from_right_file(self):

        sudoku = ''.join([str(i) for i in (numpy.array(Generator.generate_from_personals('medium')) .flatten())])
        with open('medium.txt') as f:
            lines = f.readlines()

        self.assertTrue(lines.count(sudoku + "\n") > 0)

    def test_for_generating_hard_sudoku_from_right_file(self):

        sudoku = ''.join([str(i) for i in (numpy.array(Generator.generate_from_personals('hard')) .flatten())])
        with open('hard.txt') as f:
            lines = f.readlines()

        self.assertTrue(lines.count(sudoku + "\n") > 0)

    def test_for_generating_random_easy_sudoku(self):
        sudoku = Generator.generate_random('easy')
        number_of_zeroes = sum([row.count(0) for row in sudoku])
        self.assertEqual(number_of_zeroes, Constants.EASY_LEVEL_REMOVED_DIGITS_COUNT)

    def test_for_generating_random_medium_sudoku(self):
        sudoku = Generator.generate_random('medium')
        number_of_zeroes = sum([row.count(0) for row in sudoku])
        self.assertEqual(number_of_zeroes, Constants.MEDIUM_LEVEL_REMOVED_DIGITS_COUNT)

    def test_for_generating_random_hard_sudoku(self):
        sudoku = Generator.generate_random('hard')
        number_of_zeroes = sum([row.count(0) for row in sudoku])
        self.assertEqual(number_of_zeroes, Constants.HARD_LEVEL_REMOVED_DIGITS_COUNT)


class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Grid('easy', 'random')
        self.assertTrue(hasattr(board, 'sudoku'))
        self.assertTrue(hasattr(board, 'solved_sudoku'))
        self.assertTrue(hasattr(board, 'hints_allowed'))
        self.assertTrue(hasattr(board, 'mistakes_allowed'))
        self.assertTrue(hasattr(board, 'unofficial_moves'))

    def test_hints_giving(self):

        board = Grid('medium', 'random')
        initial_zeroes_count = sum([row.count(0) for row in board.sudoku])
        board.give_hint()
        new_zeroes_count = sum([row.count(0) for row in board.sudoku])
        self.assertEqual(initial_zeroes_count, new_zeroes_count + 1)

    def test_for_is_solved(self):

        board = Grid('easy', 'random')
        self.assertFalse(board.is_solved())
        board.sudoku = board.solved_sudoku
        self.assertTrue(board.is_solved())


class TestInputValidator(unittest.TestCase):

    def test_for_is_invalid_pos_must_throw_pos_out_of_range_exception(self):

        self.assertRaises(Exceptions.PositionOutOfRangeException, IValidator.is_invalid_pos, (9, 1), 0, 9)
        self.assertRaises(Exceptions.PositionOutOfRangeException, IValidator.is_invalid_pos, (3, -1), 0, 9)
        self.assertRaises(Exceptions.PositionOutOfRangeException, IValidator.is_invalid_pos, (-2, -1), 0, 9)

    def test_for_check_hints_available_must_throw_no_more_hints_exception(self):

        self.assertRaises(Exceptions.NoMoreHintsException, IValidator.check_hints_available, 0)
        self.assertRaises(Exceptions.NoMoreHintsException, IValidator.check_hints_available, -1)

    def test_for_is_invalid_num_must_throw_num_out_of_range_exception(self):
        self.assertRaises(Exceptions.NumberOutOfRangeException, IValidator.is_invalid_num, 10, 1, 9)
        self.assertRaises(Exceptions.NumberOutOfRangeException, IValidator.is_invalid_num, 0, 1, 9)

    def test_for_invalid_confirmation_answer(self):
        self.assertRaises(Exceptions.NotAllowedConfirmationAnswerException, IValidator.is_invalid_confirmation, '')
        self.assertRaises(Exceptions.NotAllowedConfirmationAnswerException, IValidator.is_invalid_confirmation, 'shd')
        self.assertRaises(Exceptions.NotAllowedConfirmationAnswerException, IValidator.is_invalid_confirmation, ' ')

    def test_for_is_filled_pos_must_throw_already_filled_cell_exception(self):

        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.assertRaises(Exceptions.FilledCellException, IValidator.is_filled_pos, sudoku, (0, 0))

    def test_for_is_invalid_input_type_must_throw_invalid_input_type_exception(self):
        self.assertRaises(Exceptions.WrongInputTypeException, IValidator.is_invalid_input_type, '')
        self.assertRaises(Exceptions.WrongInputTypeException, IValidator.is_invalid_input_type, 'sadf')

    def test_for_is_invalid_tuple(self):
        self.assertRaises(Exceptions.InvalidTupleException, IValidator.is_invalid_tuple, ['4'])
        self.assertRaises(Exceptions.InvalidTupleException, IValidator.is_invalid_tuple, [])

    def test_for_invalid_tuple_arguments(self):
        self.assertRaises(Exceptions.InvalidTupleArgsException, IValidator.check_arguments_of_tuple, ['ere', 'ds'])


class TestEngine(unittest.TestCase):

    def test_init(self):
        engine = Engine()
        self.assertTrue(hasattr(engine, 'is_running'))


if __name__ == '__main__':
    unittest.main()
