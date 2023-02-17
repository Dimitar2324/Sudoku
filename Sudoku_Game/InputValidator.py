import Exceptions
import Constants


class IValidator:

    @staticmethod
    def check_hints_available(hints):
        if hints <= 0:
            raise Exceptions.NoMoreHintsException()

    @staticmethod
    def is_invalid_pos(position, min_limit, max_limit):

        def is_outside_grid_boundaries(dimension):
            return dimension < min_limit or dimension >= max_limit

        if is_outside_grid_boundaries(position[0]) or is_outside_grid_boundaries(position[1]):
            raise Exceptions.PositionOutOfRangeException()

    @staticmethod
    def is_filled_pos(sudoku, position):
        if sudoku[position[0]][position[1]] != 0:
            raise Exceptions.FilledCellException()

    @staticmethod
    def is_invalid_num(num, min_limit, max_limit):
        if num not in range(min_limit, max_limit):
            raise Exceptions.NumberOutOfRangeException()

    @staticmethod
    def is_invalid_confirmation(answer):
        if answer not in Constants.POSSIBLE_CONFIRMATION_ANSWERS:
            raise Exceptions.NotAllowedConfirmationAnswerException()

    @staticmethod
    def is_invalid_input_type(value):
        if not value.isnumeric():
            raise Exceptions.WrongInputTypeException

    @staticmethod
    def is_invalid_tuple(args):
        if len(args) != 2:
            raise Exceptions.InvalidTupleException

    @staticmethod
    def check_arguments_of_tuple(args):
        for arg in args:
            if not arg.isnumeric():
                raise Exceptions.InvalidTupleArgsException
