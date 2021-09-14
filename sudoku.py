def sudoku_solvable(grid, row, col):

    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] != 0:
        return sudoku_solvable(grid, row, col+1)

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if sudoku_solvable(grid, row, col+1):
                return True
        grid[row][col] = 0

    return False


def is_safe(grid, row, col, num):

    for i in range(0,9):
        if grid[row][i] == num:
            return False

    for i in range(0,9):
        if grid[i][col] == num:
            return False

    row_begin = row - (row % 3)
    col_begin = col - (col % 3)
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i+row_begin][j+col_begin] == num:
                return False

    return True


def print_grid (grid):
    for i in range(0,9):
        if i % 3 == 0 and i != 0:
            print("-------------------------------")
        for j in range(0,9):
            if j % 3 == 0 and j != 0:
                print("|", end="  ")
            print(str(grid[i][j]), end="  ")
        print()

