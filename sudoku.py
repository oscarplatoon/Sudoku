from methods import Methods

board_input = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

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
        for number in self.rows:
            for letter in self.columns:
                print(f"{letter}{number}: {self.board[f'{letter}{number}']}")
            
        
    def solve(self):
        for z in range(100):
            for number in self.rows:
                for letter in self.columns:
                    Methods.check_column(self,f'{letter}{number}')
                    Methods.check_row(self,f'{letter}{number}')
                    Methods.check_box(self,f'{letter}{number}')
        

    def board(self):
        pass

game = SudokuSolver(board_input)
game.solve()
game.print_board()

        # The file has newlines at the end of each line, so we call
        # String#chomp to remove them.
        # game = SudokuSolver(board_string)
        # # Remember: this will just fill out what it can and not "guess"
        # game.solve

        # print(game.board)
