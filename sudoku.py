import os
import csv
import random


class SudokuSolver:
    def __init__(self):
        # contains 9 row arrays that contain numbers
        self.board = [[], [], [], [], [], [], [], [], []]
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

        # adds nums to self.board
        row_index = 0
        for i, char in enumerate(initial_board_str):
            self.board[row_index].append(int(char))
            if i % 9 == 8:
                row_index += 1

    def find_next_zero(self):
        for row_index in range(9):
            for col_index in range(9):
                if self.board[row_index][col_index] == 0:
                    return (row_index, col_index)
        return None  # if no more zeroes

    def is_valid(self, guess, row_index, col_index):
        # check row
        row_vals = self.board[row_index]
        if guess in row_vals:
            return False

        # check column
        for i in range(9):
            if self.board[i][col_index] == guess:
                return False

        # check 3x3 box
        row_index_start = row_index // 3
        col_index_start = col_index // 3
        for row_index_2 in range(row_index_start, row_index_start + 3):
            for col_index_2 in range(col_index_start, col_index_start + 3):
                if self.board[row_index_2][col_index_2] == guess:
                    return False

        # if is valid
        return True

    def solve(self):
        row_index, col_index = self.find_next_zero()

        # if sudoku is solved
        if row_index is None:
            print('sudoku is solved')
            return True

        for guess in range(1, 10):
            if self.is_valid(guess, row_index, col_index):
                self.board[row_index][col_index] = guess

                if self.solve():
                    return True

            # self.board[row_index][col_index] = 0

        return False

    def print_board(self):
        print("---------------------")
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                print(num, end=" ")
                if j % 9 == 8:
                    pass
                elif j % 3 == 2:
                    print("| ", end="")
            print()
            if i % 3 == 2:
                print("---------------------")


if __name__ == "__main__":
    game = SudokuSolver()
    game.print_board()
    print()
    game.solve()
    game.print_board()
