import constants
from coloring import BColors


class NoMoreHintsException(Exception):
    def __init__(self):
        self.message = constants.HINTS_LIMIT_REACHED_MESSAGE
        super().__init__(self.message)


class PositionOutOfRangeException(Exception):
    def __init__(self):
        self.message = constants.INVALID_POSITION_MESSAGE
        super().__init__(self.message)


class FilledCellException(Exception):
    def __init__(self):
        self.message = constants.FILLED_CELL_MESSAGE
        super().__init__(self.message)


class NumberOutOfRangeException(Exception):
    def __init__(self):
        self.message = constants.INVALID_NUM_MESSAGE.format(BColors.FAIL, constants.GRID_ROWS_COLS_COUNT, BColors.ENDC)
        super().__init__(self.message)


class NotAllowedConfirmationAnswerException(Exception):
    def __init__(self):
        self.message = constants.WRONG_CONFIRMATION_ANSWER_MESSAGE
        super().__init__(self.message)


class WrongMoveException(Exception):
    def __init__(self):
        self.message = constants.WRONG_MOVE_MESSAGE
        super().__init__(self.message)


class WrongInputTypeException(Exception):
    def __init__(self):
        self.message = constants.WRONG_INPUT_TYPE_MESSAGE
        super().__init__(self.message)


class InvalidTupleException(Exception):
    def __init__(self):
        self.message = constants.INVALID_TUPLE_MESSAGE
        super().__init__(self.message)


class InvalidTupleArgsException(Exception):
    def __init__(self):
        self.message = constants.INVALID_TUPLE_ARGUMENTS_MESSAGE
        super().__init__(self.message)
