from sudoku import *
from game_boards import game_one


def main():
    if sudoku_solvable(game_one, 0, 0):
        print_grid(game_one)
    else:
        print("No solution")


main()
