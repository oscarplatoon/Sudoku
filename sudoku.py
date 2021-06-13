# import csv

class SudokuSolver:
  def __init__(self, board_string):
    self.grid = []
    self.board_string = board_string

  #setup board from input string
  def board(self):
    # for 0 - 80 stepping every 9 numbers to create 9 iterations
    for i in range(0, len(self.board_string), 9):
        #splice every 9 digits to create a list of 9 digits
        row = self.board_string[i:i+9]
        #temp list to store
        temp = []
        #for digit in row append to list and convert to int
        for num in row:
          temp.append(int(num))
        #append temp to grid to create list of lists and make the grid
        self.grid.append(temp)
  
  #helper function to print board
  def print_board(self):
    for row in self.grid:
      print(row)

  # checking if it's possible to place n in each row, column, or 3x3 grid
  def grid_check(self,r,c,n):
    # iterate through each digit in row & try to find n
    # if n is found return false..this means u can't put n in your current row
    for i in range(0,9):
      if self.grid[r][i] == n:
        return False
    # do the same thing for your current column as above
    for i in range(0,9):
      if self.grid[i][c] == n:
        return False

    # find where the 3x3 box starts  by using floor division to throw away remainder then multiply by 3 to find index
    # 1//3 = 0 -> *3 = 0 -> iterate 0 -> 3 excluding 3 with range i.e. 0,1,2
    # 5//3 = 1 -> *3 = 3 -> iterate 3 -> 6 excluding 6 with range i.e. 3,4,6
    # this lets us check the 3 x 3 grid that our self.grid[r][c] value is in
    r_start = (r//3) * 3
    c_start = (c//3) * 3
    for r in range(r_start, r_start + 3):
      for c in range(c_start,c_start + 3):
        if self.grid[r][c] == n:
          return False

    return True

  #solve function that uses recursion and backtracking
  def solve(self): 
    #double for loop to loop through every space in the grid
    for r in range(9):
      for c in range(9):
        # if a 0 (empty space) is found check what number can possibly go in there 1-9
        if self.grid[r][c] == 0:
          # n is our number that we're guessing could be correct
          for n in range(1,10):
            #if we find a number that isn't in same row, column, or grid (if grid_check returns true)
            if self.grid_check(r,c,n):
              #set the space in grid equal to number
              self.grid[r][c] = n
              #call solve fxn again recursively
              self.solve()
              #if we get to a point where solve cannot place the final number it will assign it to 0 and check the next number
              # eventually when we get to a dead end we'll return all the way to the first solve() call and try the next n in range 1,10
              # and then we'll start the recursive cycle all over again until we either solve the puzzle or
              # have to backtrack again
              self.grid[r][c] = 0
          return
    #print solved board
    self.print_board()


game = SudokuSolver('000020040008035000000070602031046970200000000000501203049000730000000010800004000')
game.board()
game.solve()

