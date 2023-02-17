import Constants
from Coloring import bcolors


class Drawer:

    @staticmethod
    def draw_grid(grid, moves):
        for i in range(Constants.GRID_ROWS_COLS_COUNT):

            if i % 3 == 0:
                print("|-----------------------|")
            for j in range(Constants.GRID_ROWS_COLS_COUNT):
                if j % 3 == 0:
                    print("| ", end="")

                if j == Constants.GRID_ROWS_COLS_COUNT - 1:

                    if (i, j) not in moves.keys():
                        print(grid[i][j], end=" |\n")
                    else:
                        print(f"{bcolors.OKGREEN}{moves[(i,j)]}{bcolors.ENDC}", end=" |\n")
                else:

                    if (i, j) not in moves.keys():
                        print(f"{grid[i][j]} ", end="")
                    else:
                        print(f"{bcolors.OKGREEN}{moves[(i, j)]}{bcolors.ENDC} ", end="")

            if i + 1 == Constants.GRID_ROWS_COLS_COUNT:
                print("|-----------------------|")
