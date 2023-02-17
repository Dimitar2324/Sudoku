from Coloring import bcolors

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
WRONG_CONFIRMATION_ANSWER_MESSAGE = f'{bcolors.FAIL}Confirmation answers are either yes or no!{bcolors.ENDC}'
WRONG_MOVE_MESSAGE = f'{bcolors.FAIL}Wrong answer!{bcolors.ENDC}'
FILLED_CELL_MESSAGE = f'{bcolors.FAIL}Cannot modify initial value or values that are correct! Try again.{bcolors.ENDC}'
INVALID_POSITION_MESSAGE = f'{bcolors.FAIL}Invalid position! Try again.{bcolors.ENDC}'
HINTS_LIMIT_REACHED_MESSAGE = f'{bcolors.FAIL}No more hints allowed. Think more carefully!{bcolors.ENDC}'
INVALID_NUM_MESSAGE = '{0}Choose nums in range 1-{1}! Try again.{2}'
LOSING_MESSAGE = 'Sorry, better luck next time! The solved sudoku is: '
WINNING_MESSAGE = f'{bcolors.OKCYAN}Congratulations! You solved the puzzle!{bcolors.ENDC}'
WRONG_INPUT_TYPE_MESSAGE = f'{bcolors.FAIL}Input must be an integer!{bcolors.ENDC}'
INVALID_TUPLE_MESSAGE = f'{bcolors.FAIL}Input must be a tuple - (x ,y) or 10 for hint!{bcolors.ENDC}'
INVALID_TUPLE_ARGUMENTS_MESSAGE = f'{bcolors.FAIL}Tuple arguments must be integers!{bcolors.ENDC}'
