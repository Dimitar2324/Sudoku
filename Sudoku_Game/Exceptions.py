import Constants
from Coloring import bcolors


class NoMoreHintsException(Exception):
    def __init__(self):
        self.message = Constants.HINTS_LIMIT_REACHED_MESSAGE
        super().__init__(self.message)


class PositionOutOfRangeException(Exception):
    def __init__(self):
        self.message = Constants.INVALID_POSITION_MESSAGE
        super().__init__(self.message)


class FilledCellException(Exception):
    def __init__(self):
        self.message = Constants.FILLED_CELL_MESSAGE
        super().__init__(self.message)


class NumberOutOfRangeException(Exception):
    def __init__(self):
        self.message = Constants.INVALID_NUM_MESSAGE.format(bcolors.FAIL, Constants.GRID_ROWS_COLS_COUNT, bcolors.ENDC)
        super().__init__(self.message)


class NotAllowedConfirmationAnswerException(Exception):
    def __init__(self):
        self.message = Constants.WRONG_CONFIRMATION_ANSWER_MESSAGE
        super().__init__(self.message)


class WrongMoveException(Exception):
    def __init__(self):
        self.message = Constants.WRONG_MOVE_MESSAGE
        super().__init__(self.message)


class WrongInputTypeException(Exception):
    def __init__(self):
        self.message = Constants.WRONG_INPUT_TYPE_MESSAGE
        super().__init__(self.message)


class InvalidTupleException(Exception):
    def __init__(self):
        self.message = Constants.INVALID_TUPLE_MESSAGE
        super().__init__(self.message)


class InvalidTupleArgsException(Exception):
    def __init__(self):
        self.message = Constants.INVALID_TUPLE_ARGUMENTS_MESSAGE
        super().__init__(self.message)
