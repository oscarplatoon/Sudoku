from methods import Methods
import os
import csv

board = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

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

    def print_board(self,board):
        for number in self.rows:
            for letter in self.columns:
                if len(self.board[f'{letter}{number}']) != 1:
                    print(f'Fail: {board}')
                    # for number in self.rows:
                    #     for letter in self.columns:
                    #         print(f"{letter}{number}: {self.board[f'{letter}{number}']}")
                    
                    return(False)            
        return(True)
        
            
        
    def solve(self):
        for z in range(10):
            for number in self.rows:
                for letter in self.columns:
                    Methods.check_column(self,f'{letter}{number}')
                    Methods.check_row(self,f'{letter}{number}')
                    Methods.check_box(self,f'{letter}{number}')
            Methods.naked_subset_rows(self)
            Methods.naked_subset_columns(self)
            Methods.naked_subset_box(self)
            Methods.hidden_subset_rows(self)
            Methods.hidden_subset_columns(self)
            Methods.hidden_subset_box(self)
            Methods.x_wing_row(self)
            # Methods.swordfish(self)
            

    def board_out(self):
        o = self.board
        print(
            '---------------------\n'
            f"{o['a1'][0]} {o['a2'][0]} {o['a3'][0]} | {o['a4'][0]} {o['a5'][0]} {o['a6'][0]} | {o['a7'][0]} {o['a8'][0]} {o['a9'][0]}\n"
            f"{o['b1'][0]} {o['b2'][0]} {o['b3'][0]} | {o['b4'][0]} {o['b5'][0]} {o['b6'][0]} | {o['b7'][0]} {o['b8'][0]} {o['b9'][0]}\n"
            f"{o['c1'][0]} {o['c2'][0]} {o['c3'][0]} | {o['c4'][0]} {o['c5'][0]} {o['c6'][0]} | {o['c7'][0]} {o['c8'][0]} {o['c9'][0]}\n"
            '---------------------\n'
            f"{o['d1'][0]} {o['d2'][0]} {o['d3'][0]} | {o['d4'][0]} {o['d5'][0]} {o['d6'][0]} | {o['d7'][0]} {o['d8'][0]} {o['d9'][0]}\n"
            f"{o['e1'][0]} {o['e2'][0]} {o['e3'][0]} | {o['e4'][0]} {o['e5'][0]} {o['e6'][0]} | {o['e7'][0]} {o['e8'][0]} {o['e9'][0]}\n"
            f"{o['f1'][0]} {o['f2'][0]} {o['f3'][0]} | {o['f4'][0]} {o['f5'][0]} {o['f6'][0]} | {o['f7'][0]} {o['f8'][0]} {o['f9'][0]}\n"
            '---------------------\n'
            f"{o['g1'][0]} {o['g2'][0]} {o['g3'][0]} | {o['g4'][0]} {o['g5'][0]} {o['g6'][0]} | {o['g7'][0]} {o['g8'][0]} {o['g9'][0]}\n"
            f"{o['h1'][0]} {o['h2'][0]} {o['h3'][0]} | {o['h4'][0]} {o['h5'][0]} {o['h6'][0]} | {o['h7'][0]} {o['h8'][0]} {o['h9'][0]}\n"
            f"{o['i1'][0]} {o['i2'][0]} {o['i3'][0]} | {o['i4'][0]} {o['i5'][0]} {o['i6'][0]} | {o['i7'][0]} {o['i8'][0]} {o['i9'][0]}\n"
        )
        

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

game = SudokuSolver(board)
game.solve()
print(f'\nMain Test case(input:{board})')
game.board_out()

print(f'\nFor all test cases')
for x in input_boards:
    game = SudokuSolver(x[0])
    game.solve()
    if game.print_board(x) == True:
        solved_count += 1
    else:
        failed_count += 1
print(f'Solved: {solved_count}\tFailed: {failed_count}')




