import Constants
import DrawingManager
import SudokuGenerator
from copy import deepcopy

'''
Official last version

import random
import Constants
from SudokuSolver import Solver
from SudokuGenerator import Generator
from DrawingManager import Drawer
from copy import deepcopy
from Coloring import bcolors


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

        row = random.randint(0, len(self.sudoku) - 1)
        col = random.randint(0, len(self.sudoku) - 1)

        while self.sudoku[row][col] != 0:
            row = random.randint(0, len(self.sudoku) - 1)
            col = random.randint(0, len(self.sudoku) - 1)

        self.sudoku[row][col] = self.solved_sudoku[row][col]
        if (row, col) in self.unofficial_moves.keys():
            self.unofficial_moves.pop((row, col))

    def is_outside_grid_boundaries(self, dimension):
        return dimension < 0 or dimension >= len(self.sudoku)

    def is_solved(self):

        for i in range(len(self.sudoku)):
            for j in range(len(self.sudoku[0])):
                if self.sudoku[i][j] != self.solved_sudoku[i][j]:
                    return False

        return True

    def is_filled(self, position):
        return self.sudoku[position[0]][position[1]] != 0

    def is_not_valid_number(self, candidate):
        return candidate not in range(1, len(self.sudoku) + 1)

    def start(self):
        while self.mistakes_allowed > 0 and not self.is_solved():

            Drawer.draw_grid(self.sudoku, self.unofficial_moves)

            current_move = input('Enter position or number 10 for hint: ')

            if current_move == Constants.HINT_WANTED:
                if self.hints_allowed > 0:
                    self.give_hint()
                    self.hints_allowed -= 1
                else:
                    print(f'{bcolors.FAIL}No more hints allowed. Think more carefully!{bcolors.ENDC}')

                continue

            position = tuple(int(item) - 1 for item in current_move.split())

            if self.is_outside_grid_boundaries(position[0]) or self.is_outside_grid_boundaries(position[1]):
                print(f'{bcolors.FAIL}Invalid position! Try again.{bcolors.ENDC}')
                continue

            if self.is_filled(position):
                print(f'{bcolors.FAIL}Cannot modify initial value or values that are correct! Try again.{bcolors.ENDC}')
                continue

            current_candidate = int(input('Enter your num: '))

            if self.is_not_valid_number(current_candidate):
                print(f'{bcolors.FAIL}Choose from nums in range 1-{len(self.sudoku)}! Try again.{bcolors.ENDC}')
                continue

            confirmation = input('With pencil: ')

            if confirmation == 'no':
                if self.solved_sudoku[position[0]][position[1]] == current_candidate:
                    self.sudoku[position[0]][position[1]] = current_candidate

                    if position in self.unofficial_moves.keys():
                        self.unofficial_moves.pop(position)
                else:
                    self.mistakes_allowed -= 1
                    if position in self.unofficial_moves.keys():
                        self.unofficial_moves.pop(position)

                    print(f'{bcolors.FAIL}Wrong answer!{bcolors.ENDC}')
            elif confirmation == 'yes':
                self.unofficial_moves[position] = current_candidate

        if self.mistakes_allowed == 0:
            print("Sorry, better luck next time! The solved sudoku is: ")
            self.unofficial_moves.clear()
            Drawer.draw_grid(self.solved_sudoku, self.unofficial_moves)
        else:
            print(f'{bcolors.OKCYAN}Congratulations! You solved the puzzle!{bcolors.ENDC}')



'''






""""
initial = SudokuGenerator.Generator.generate_random('easy')
copy_board = deepcopy(initial)
copy_board[0][0] = 100
DrawingManager.Drawer.draw_grid(initial)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
DrawingManager.Drawer.draw_grid(copy_board)
"""

"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
"""

# import random

"""
from SudokuSolver import Solver
from SudokuGenerator import Generator
from DrawingManager import Drawer
from copy import deepcopy


def give_hint(playing_board, solved_board):

    row = random.randint(0, len(playing_board) - 1)
    col = random.randint(0, len(playing_board) - 1)

    while playing_board[row][col] != 0:
        row = random.randint(0, len(playing_board) - 1)
        col = random.randint(0, len(playing_board) - 1)

    playing_board[row][col] = solved_board[row][col]


def is_outside_grid_boundaries(dimension, board):
    return dimension < 0 or dimension >= len(board)


def is_solved(first, second):

    for i in range(len(first)):
        for j in range(len(first[0])):
            if first[i][j] != second[i][j]:
                return False

    return True
    
    
sudoku = Generator.generate_random(difficulty_level) if type_of_sudoku == 'random' \
        else Generator.generate_from_personals(difficulty_level)

    solved_sudoku = deepcopy(sudoku)
    Solver.solve(solved_sudoku)
    hints_allowed = 3
    mistakes_allowed = 3
    unofficial_moves = {}

    while mistakes_allowed > 0 and not is_solved(sudoku, solved_sudoku):

        Drawer.draw_grid(sudoku, unofficial_moves)

        current_move = input('Enter position or 10 for hint: ')

        if current_move == '10':
            if hints_allowed > 0:
                give_hint(sudoku, solved_sudoku)
                hints_allowed -= 1
            else:
                print('No more hints allowed. Think more carefully!')

            continue

        position = tuple(int(item) for item in current_move.split())

        if is_outside_grid_boundaries(position[0], sudoku) or is_outside_grid_boundaries(position[1], sudoku):
            print('Invalid position! Try again.')
            continue

        if sudoku[position[0]][position[1]] != 0:
            print('Cannot modify initial value or values that are correct! Try again.')
            continue

        current_candidate = int(input('Enter your num: '))

        if current_candidate not in range(1, len(sudoku) + 1):
            print(f'Choose from nums in range 1-{len(sudoku)}! Try again.')
            continue

        confirmation = input('With pencil: ')

        if confirmation == 'no':
            if solved_sudoku[position[0]][position[1]] == current_candidate:
                sudoku[position[0]][position[1]] = current_candidate

                if position in unofficial_moves.keys():
                    unofficial_moves.pop(position)
            else:
                mistakes_allowed -= 1
                print('Wrong answer!')
        elif confirmation == 'yes':
            unofficial_moves[position] = current_candidate

    if mistakes_allowed == 0:
        print("Sorry, better luck next time! The solved sudoku is: ")
        unofficial_moves.clear()
        Drawer.draw_grid(solved_sudoku, unofficial_moves)
    else:
        print('Congratulations! You solved the puzzle!')
        
        
    from Board import Grid
from Coloring import bcolors


def show_menu():
    print('Chose the number of one of the following:')
    print('  1. Start new game')
    print('  2. Quit')


def start_game():

    while True:
        difficulty_level = input('Choose difficulty level: ').lower()
        type_of_sudoku = input('From personal collection or random: ').lower()

        if difficulty_level not in ('easy', 'medium', 'hard') or type_of_sudoku not in ('random', 'personal'):
            print(f'{bcolors.FAIL}Difficulty level must be easy/medium/hard.'
                  f'Sudoku type must be random/personal!{bcolors.ENDC}')
            continue

        break

    grid = Grid(difficulty_level, type_of_sudoku)
    grid.start()


is_running = True

while is_running:

    show_menu()
    choice = int(input('Your choice: '))
    if choice not in (1, 2):
        continue
    elif choice == 1:
        start_game()
    else:
        is_running = False
"""

'''
4 3 2 | 6 1 5 | 7 8 9 |
| 7 5 1 | 8 2 9 | 4 3 6 |
| 8 6 9 | 3 7 4 | 1 2 5 |
|-----------------------|
| 1 8 5 | 4 6 2 | 9 7 3 |
| 2 4 3 | 5 9 7 | 8 6 1 |
| 6 9 7 | 1 8 3 | 5 4 2 |
|-----------------------|
| 3 1 6 | 9 4 8 | 2 5 0 |
| 5 2 4 | 7 3 1 | 6 9 8 |
| 9 7 8 | 2 5 6 | 3 1 4 |
'''

