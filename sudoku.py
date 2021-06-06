import os
import csv
import random


class SudokuSolver:
    def __init__(self):
        self.board = []  # contains Cell objects
        initial_board_states = []

        # fills out initial_board_states as strings of nums
        dir_path = os.getcwd()
        csv_path = os.path.join(dir_path, './sample_sudoku_board_inputs.csv')
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                initial_board_states.append(line[0])

        # gets a random board and assigns it
        rand_board_index = random.randrange(len(initial_board_states))
        initial_board_str = initial_board_states[rand_board_index]
        for char in initial_board_str:
            self.board.append(Cell(int(char)))

    def solve(self):
        pass

    def print_board(self):
        print("---------------------")
        for i, cell in enumerate(self.board):
            print(cell.num, end=" ")
            if i % 9 == 8:
                print()
            elif i % 3 == 2:
                print("", end="| ")
            if i % 27 == 26:
                print("---------------------")


class Cell:
    def __init__(self, num) -> None:
        self.num = num

    def get_other_row_cells(self):
        pass

    def get_other_column_cells(self):
        pass

    def get_other_box_cells(self):
        pass


game = SudokuSolver()
game.print_board()
# game.solve
# game.print_board()
