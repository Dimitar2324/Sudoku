from coloring import BColors

EASY_LEVEL_REMOVED_DIGITS_COUNT = 6
MEDIUM_LEVEL_REMOVED_DIGITS_COUNT = 12
HARD_LEVEL_REMOVED_DIGITS_COUNT = 18
DIFFICULTY_LEVELS = ('easy', 'medium', 'hard')
SUDOKU_TYPES = ('random', 'personal')
POSSIBLE_CONFIRMATION_ANSWERS = ('yes', 'no')
MENU_OPPORTUNITIES = (1, 2)
ALLOWED_MISTAKES_PER_GAME = 3
ALLOWED_HINTS_PER_GAME = 3
HINT_WANTED = '10'
GRID_ROWS_COLS_COUNT = 9
WRONG_CONFIRMATION_ANSWER_MESSAGE = f'{BColors.FAIL}Confirmation answers are either yes or no!{BColors.ENDC}'
WRONG_MOVE_MESSAGE = f'{BColors.FAIL}Wrong answer!{BColors.ENDC}'
FILLED_CELL_MESSAGE = f'{BColors.FAIL}Cannot modify initial value or values that are correct! Try again.{BColors.ENDC}'
INVALID_POSITION_MESSAGE = f'{BColors.FAIL}Invalid position! Try again.{BColors.ENDC}'
HINTS_LIMIT_REACHED_MESSAGE = f'{BColors.FAIL}No more hints allowed. Think more carefully!{BColors.ENDC}'
INVALID_NUM_MESSAGE = '{0}Choose nums in range 1-{1}! Try again.{2}'
LOSING_MESSAGE = 'Sorry, better luck next time! The solved sudoku is: '
WINNING_MESSAGE = f'{BColors.OKCYAN}Congratulations! You solved the puzzle!{BColors.ENDC}'
WRONG_INPUT_TYPE_MESSAGE = f'{BColors.FAIL}Input must be an integer!{BColors.ENDC}'
INVALID_TUPLE_MESSAGE = f'{BColors.FAIL}Input must be a tuple - (x ,y) or 10 for hint!{BColors.ENDC}'
INVALID_TUPLE_ARGUMENTS_MESSAGE = f'{BColors.FAIL}Tuple arguments must be integers!{BColors.ENDC}'
