import constants
from coloring import BColors


class DrawingManager:

    @staticmethod
    def draw_grid(grid, moves):
        for i in range(constants.GRID_ROWS_COLS_COUNT):

            if i % 3 == 0:
                print("|-----------------------|")
            for j in range(constants.GRID_ROWS_COLS_COUNT):
                if j % 3 == 0:
                    print("| ", end="")

                if j == constants.GRID_ROWS_COLS_COUNT - 1:

                    if (i, j) not in moves.keys():
                        print(grid[i][j], end=" |\n")
                    else:
                        print(f"{BColors.OKGREEN}{moves[(i, j)]}{BColors.ENDC}", end=" |\n")
                else:

                    if (i, j) not in moves.keys():
                        print(f"{grid[i][j]} ", end="")
                    else:
                        print(f"{BColors.OKGREEN}{moves[(i, j)]}{BColors.ENDC} ", end="")

            if i + 1 == constants.GRID_ROWS_COLS_COUNT:
                print("|-----------------------|")
