from modules.sudoku import SudokuSolver
import os
import csv

def read_sudoku_boards():
        boards = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./data/sample_sudoku_board_inputs.csv")

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                boards.append(SudokuSolver(*row))

        return boards

def solve_list_sudoku_boards(boards_list):
        for board in boards_list:
                board = board.solve()
        return boards_list

def write_sudoku_boards(boards_to_write):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./data/sample_sudoku_board_solutions.csv")

        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for board in boards_to_write:
                output = ''.join([str(elem) for elem in board.board])
                writer.writerow([output])


my_boards = read_sudoku_boards()
my_solved_boards = solve_list_sudoku_boards(my_boards)
write_solved_boards = write_sudoku_boards(my_solved_boards)