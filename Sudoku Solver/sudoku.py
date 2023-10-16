import curses
from curses import wrapper

sudoku = [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]

N=9

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

def print_game(sudoku, stdscr, matrix=[]):
    WHITE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if (i,j) in matrix:
                stdscr.addstr(i, j*2, value, RED)
            else:
                stdscr.addstr(i, j*2, value, WHITE)

def check_valid_grid(sudoku, row, column, cell):
    #Checking if number is in same row
    for x in range(9):
        if sudoku[row][x] == cell:
            return False
    #Checking if number is in same column
    for x in range(9):
        if sudoku[column][x] == cell:
            return False