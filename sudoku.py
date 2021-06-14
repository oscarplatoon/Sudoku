from IPython import embed
import csv
import itertools

class Sudoku():
    def __init__(self, board_string):
        self.board_string = board_string
        self.print_board()

    def solve(self):
        try:
            # try to find the next index that has a missing number, represented by the string '0' per the instructions
            next_missing_number_index = self.board_string.index('0')
        except ValueError:
            # if you can't find any indexes with '0' on the board, then it's fully solved and you can exit
            return True

        for possible_move in range(1, 10):
            self.board_string = self.generate_possible_board(next_missing_number_index, possible_move)

            # if it's a legitimate board with that possible move, then we recursively call the method again with the next missing number's index

            if self.legitimate_board(next_missing_number_index) == True and self.solve():
                return self.board_string

        # if you go through the possible numbers (1-9) and can't get an answer, that means you have to go back out one level and try the next number and then the other 1-9 combinations from there.

        self.board_string = self.generate_possible_board(next_missing_number_index, '0')
        return False

    def generate_possible_board(self, next_missing_number_index, possible_move):
        output = self.board_string[0:next_missing_number_index] # first half
        last_half = self.board_string[next_missing_number_index + 1:]
        output += str(possible_move)
        output += last_half
        return output

    def legitimate_board(self, index_of_number):
        number_to_try = self.board_string[index_of_number]
        if self.legitimate_row(number_to_try, index_of_number) == False or self.legitimate_column(number_to_try, index_of_number) == False or self.legitimate_grid(number_to_try, index_of_number) == False:
            return False
        else:
            return True

    def legitimate_row(self, number, index_of_number):
        row = index_of_number // 9
        shift_amount = row * 9
        for check_index in range(shift_amount, shift_amount + 9):
            if self.valid(check_index, number, index_of_number) != True:
                return False

    def legitimate_column(self, number, index_of_number):
        column = index_of_number % 9
        start = 0
        for _ in itertools.repeat(None, 9):
            check_index = start + column
            if self.valid(check_index, number, index_of_number) != True:
                return False
            start += 9

    def legitimate_grid(self, number, index_of_number):
        column_start = index_of_number % 9 // 3 * 3
        row_start = index_of_number // 27 * 27

        for _ in itertools.repeat(None, 3):
            for column in range(column_start, column_start + 3):
                if self.valid(column + row_start, number, index_of_number) != True:
                    return False
            row_start += 9

    def valid(self, index, number, index_of_number):
        if index != index_of_number and number == self.board_string[index]:
            return False
        else:
            return True

    def print_board(self):
        output_string = ''

        for index, character in enumerate(self.board_string):
            # create a variable so you can count like a human starting at 1 instead of 0
            character_index = index + 1

            # print dashes for each 9x3 section for visualization
            if index % 27 == 0:
                output_string += '-' * 23 + "\n"

            # for the beginning board, replace all 0's with spaces and space out the other numbers
            if character == '0':
                output_string += "   "
            else:
                output_string += f"{character} "

            # put pipes after every 3rd and 6th character
            if character_index % 9 == 3 or  character_index % 9 == 6:
                output_string += " | "

            # put a newline after every 9th character
            if character_index % 9 == 0:
                output_string += "\n"

        return output_string

with open('sample_sudoku_board_inputs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for index, row in enumerate(csv_reader):
        print(f'{index+1} out of 50')
        s = Sudoku(row[0])
        s.solve()
        print(s.print_board())
