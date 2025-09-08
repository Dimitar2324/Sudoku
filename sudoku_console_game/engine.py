import constants
from board import Board
from coloring import BColors
from input_validator import InputValidator


class Engine:

    def __init__(self):
        self.is_running = True

    @staticmethod
    def show_menu():
        print('Chose the number of one of the following:')
        print('  1. Start new game')
        print('  2. Quit')

    @staticmethod
    def start_game():

        while True:
            difficulty_level = input('Choose difficulty level: ').lower()
            type_of_sudoku = input('From personal collection or random: ').lower()

            if difficulty_level not in constants.DIFFICULTY_LEVELS or type_of_sudoku not in constants.SUDOKU_TYPES:
                print(f'{BColors.FAIL}Difficulty level must be easy/medium/hard.'
                      f'Sudoku type must be random/personal!{BColors.ENDC}')
                continue

            break

        grid = Board(difficulty_level, type_of_sudoku)
        grid.start()

    def run(self):

        while self.is_running:

            try:
                self.show_menu()
                str_choice = input('Your choice: ')
                InputValidator.is_invalid_input_type(str_choice)

                choice = int(str_choice)
                if choice not in constants.MENU_OPPORTUNITIES:
                    continue

                if choice == 1:
                    self.start_game()
                else:
                    self.is_running = False
            except Exception as ex:
                print(ex)
