
class SudokuSolver:
  def __init__(self, board_string):
    self.board = [int(i) for i in board_string]
    self.empty_cells_and_attempts = [[i, []] for i, elem in enumerate(self.board) if elem == 0]
    print(self.empty_cells_and_attempts)

  def solve(self):
    pass

  def board(self):
    pass

  # returns an ordered list of elements in ROW_NUMBER
  # for row 0: 0,1,2,3,4,5,6,7,8
  # for row 1: 9,10,11,12,13,14,15,16,17
  def get_row(self, row_number):
    output_row = []
    for i in range(row_number*9, (row_number*9)+9):
      output_row.append(self.board[i])
    return output_row

  # returns an ordered list of elements in COLUMN_NUMBER
  # for column 0: 0,9,18,27,36,45,54,63,72
  # for column 1: 1,10,19,28,37,46,55,64,73
  def get_column(self, column_number):
    output_column = []
    for i in range(column_number, column_number+73, 9):
      output_column.append(self.board[i])
    return output_column

  # returns an ordered list of elements in a square
  # squares are referenced by their upper-left most element
  # so squares references are 0, 3, 6, 27, 30, 33, 54, 57, 60
  # the square referenced by 0 contains elements at indices
  # 0, 1, 2, 9, 10, 11, 18, 19, 20
  # the square referenced by 33 contains elements at indices
  # 33, 34, 35, 42, 43, 44, 51, 52, 53
  def get_square(self, square_index):
    output_square = []
    i = square_index
    while i < square_index+21:
      output_square.append(self.board[i])
      if len(output_square) % 3 == 0:
        i += 6
      i += 1
    return output_square
  
  # check_row takes in an ELEM and ROW_LIST
  # ROW_LIST is an ordered list of elements in
  # a row
  def check_row(self, row_list, elem):
    try:
      if row_list.index(elem) >= 0:
        return True
    except ValueError:
      return False

  def check_column(self, column_list, elem):
    try:
      if column_list.index(elem) >= 0:
        return True
    except ValueError:
      return False

  def check_square(self, square_list, elem):
    try:
      if square_list.index(elem) >= 0:
        return True
    except ValueError:
      return False

  def __str__(self):
    output_string = '-----------------------\n'
    for i, num in enumerate(self.board):
      output_string += f"{num} "
      if (i+1) % 9 == 0:
        output_string += "\n"
      elif (i+1) % 3 == 0:
        output_string += " | "
      if (i+1) % 27 == 0:
        output_string += '-----------------------\n'
    return output_string
  

# my_solver = SudokuSolver('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
# print(my_solver)
# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve

# print(game.board)
