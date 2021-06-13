from methods import Methods
import os
import csv

board_input = '030050040008010500460000012070502080000603000040109030250000098001020600080060020'

class SudokuSolver:
    # board represented as a grid a1 through i9
    # each square is a dictionary whose values correspond to all of the possibile answers for that square
    # loop through the board to try and eliminate possible answers untill only one remains

    def __init__(self, board_string):
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.quadrants ={
            '1' : [['a','b','c'],['1','2','3']],'2' : [['d','e','f'],['1','2','3']],'3' : [['g','h','i'],['1','2','3']],
            '4' : [['a','b','c'],['4','5','6']],'5' : [['d','e','f'],['4','5','6']],'6' : [['g','h','i'],['4','5','6']],
            '7' : [['a','b','c'],['7','8','9']],'8' : [['d','e','f'],['7','8','9']],'9' : [['g','h','i'],['7','8','9']],
        }
        self.count = 0
        self.board = {}
        for number in self.rows:
            for letter in self.columns:
                if board_string[self.count] == '0':
                    self.board.update({f'{letter}{number}': [x for x in range(1,10)]})
                else:
                    self.board.update({f'{letter}{number}': [int(board_string[self.count])]})
                self.count += 1

    def print_board(self):
        # for number in self.rows:
        #     for letter in self.columns:
        #         print(f"{letter}{number}: {self.board[f'{letter}{number}']}")
        for number in self.rows:
            for letter in self.columns:
                if len(self.board[f'{letter}{number}']) != 1:
                    return(False)            
        return(True)
        
            
        
    def solve(self):
        for z in range(100):
            for number in self.rows:
                for letter in self.columns:
                    Methods.check_column(self,f'{letter}{number}')
                    Methods.check_row(self,f'{letter}{number}')
                    Methods.check_box(self,f'{letter}{number}')
            Methods.naked_subset_rows(self)
            Methods.naked_subset_columns(self)
            Methods.naked_subset_box(self)
            Methods.hidden_subset_rows(self)
            Methods.hidden_subset_rows(self)
            

    def board(self):
        pass

    @classmethod
    def objects(cls):
        input_boards = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "sample_sudoku_board_inputs.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                input_boards.append(row)
        return input_boards

input_boards = SudokuSolver.objects()
solved_count, failed_count = 0,0
for x in input_boards:
    game = SudokuSolver(x[0])
    game.solve()
    if game.print_board() == True:
        solved_count += 1
    elif game.print_board() == False:
        failed_count += 1
print(f'Solved: {solved_count}\tFailed: {failed_count}')



        # print(game.board)
