from sudoku import SudokuSolver
import os
import csv

def read_sudoku_board():

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "single_sudoku_board.csv")

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                board = SudokuSolver(*row)


        return board

my_board = read_sudoku_board()
print(my_board)
# print(my_board.get_row(7))
# print(my_board.get_column(4))
# my_row = my_board.get_row(0)
# print(my_board.check_row(my_row, 1))