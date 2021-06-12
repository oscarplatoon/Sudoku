import os
import csv

class SudokuSolver:
  def __init__(self, board_string):
    self.board = [int(i) for i in board_string]
    self.empty_cells_and_attempts = [[i, []] for i, elem in enumerate(self.board) if elem == 0]
    self.square_indices = self.read_in_square_indices()
    self.row_indices = self.read_in_row_indices()
    self.column_indices = self.read_in_column_indices()
  
  def solve(self):
    
    index_of_current_empty_cell_to_guess = 0
    # while True:
    for i in range(10000):
      current_attempt = self.get_next_attempt(index_of_current_empty_cell_to_guess)
      current_board_index = self.empty_cells_and_attempts[index_of_current_empty_cell_to_guess][0]

      if current_attempt == None:
        if index_of_current_empty_cell_to_guess == 0:
          print("This puzzle has no solution")
          return None
        else:
          self.clear_all_attempts(index_of_current_empty_cell_to_guess)
          index_of_current_empty_cell_to_guess -= 1
      # if you go back to the last cell because this one was invalid, you need to clear its guess from the board
          self.board[current_board_index] = 0
          continue
      
    
      current_row_indice = self.get_row_index_from_indice(current_board_index)
      current_column_indice = self.get_column_number_from_indice(current_board_index)
      current_square_indice = self.get_square_number_from_indice(current_board_index)

      current_row_list = self.get_row(current_row_indice)
      current_column_list = self.get_column(current_column_indice)
      current_square_list = self.get_square(current_square_indice)


      if not self.check_row(current_row_list, current_attempt) and not self.check_column(current_column_list, current_attempt) and not self.check_square(current_square_list, current_attempt):

        self.board[current_board_index] = current_attempt
        if index_of_current_empty_cell_to_guess != len(self.empty_cells_and_attempts)-1:
          index_of_current_empty_cell_to_guess += 1
        else:
          print("Puzzle solved!!!")
          return True
          

      # print(f"current attempt {current_attempt}, current_cell: {self.empty_cells_and_attempts[index_of_current_empty_cell_to_guess][0]}")

    # Set current_cell_to_guess = 0
    # this will be used to track the current_guess
    # Loop through the list of empty cells iteratively (as tracked by current_cell_to_guess) until the last cell's guess is valid
        # 1. For the current_cell_to_guess, get current_attempt (equals last value in current_attempt+1)
        # 2. If current_attempt < 10, continue, else delete all attempts from current_cell_to_guess, and decrement current_cell_to_guess to go back to the last guess, unless you are on current_cell_guess[0], then quit with error that the puzzle is unsolvable
        # 2. append current_attempt to self.empty_cells_and_attempts[current_cell_guess]
        # 3. Check row, column, and square for current cell and current attempt
        # 4. if valid, update board and increment current_cell_to_guess
        # 5. current_attempt is invalid, return to 1 
  

  # returns an ordered list of elements in row_index
  # for row 0: 0,1,2,3,4,5,6,7,8
  # for row 1: 9,10,11,12,13,14,15,16,17
  def get_row(self, row_index):
    output_row = []

    for i in range (row_index,  row_index+9):
      output_row.append(self.board[i])
    return output_row

  # returns an ordered list of elements in COLUMN_NUMBER
  # for column 0: 0,9,18,27,36,45,54,63,72
  # for column 1: 1,10,19,28,37,46,55,64,73
  def get_column(self, column_index):
    output_column = []
    for i in range(column_index, column_index+73, 9):
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
  
  def get_next_attempt(self, index):
    if len(self.empty_cells_and_attempts[index][1]) == 0:
        current_attempt = 1
        self.empty_cells_and_attempts[index][1].append(current_attempt)
        return current_attempt
    elif len(self.empty_cells_and_attempts[index][1]) == 9:
      return None
    else:
      current_attempt = self.empty_cells_and_attempts[index][1][-1] + 1
      self.empty_cells_and_attempts[index][1].append(current_attempt)
      return current_attempt

  def clear_all_attempts(self, index):
    self.empty_cells_and_attempts[index][1] = []

  def read_in_row_indices(self):
    row_indices_list = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "./data/row_indices.csv")

    with open(path, mode = 'r', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        row = [int(i) for i in row]
        row_indices_list.append(row)
    
    return row_indices_list
        
  def read_in_column_indices(self):
    column_indices_list = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "./data/column_indices.csv")

    with open(path, mode = 'r', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        row = [int(i) for i in row]
        column_indices_list.append(row)
    
    return column_indices_list

  def read_in_square_indices(self):
    square_indices_list = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "./data/square_indices.csv")

    with open(path, mode = 'r', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        row = [int(i) for i in row]
        square_indices_list.append(row)

    
    return square_indices_list

  # takes an an index anywhere on the board and returns the leading character in that index's row
  # returns None if the indice isn't found
  def get_row_index_from_indice(self, cell_index):
    for row_list_index in self.row_indices:
      try:
        if row_list_index.index(cell_index) >= 0:
          return row_list_index[0]
      except ValueError:
        pass

    return None

  def get_column_number_from_indice(self, cell_index):
    for column_list_index in self.column_indices:
      try:
        if column_list_index.index(cell_index) >= 0:
          return column_list_index[0]
      except ValueError:
        pass

    return None

  def get_square_number_from_indice(self, cell_index):
    for square_list_index in self.square_indices:
      try:
        if square_list_index.index(cell_index) >= 0:
          return square_list_index[0]
      except ValueError:
        pass

    return None

my_solver = SudokuSolver('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
print(my_solver)

my_solver.solve()
print(my_solver)
# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve
# print(my_solver.get_row(18))
# print(my_solver.get_column(5))
# print(my_solver.get_square(57))