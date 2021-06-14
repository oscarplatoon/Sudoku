import csv  # needed so we can read in the .csv file for the challenge (https://docs.python.org/3/library/csv.html)
import itertools  # needed to compute the cartesian product of input iterables (https://docs.python.org/2/library/itertools.html)


class SudokuSolver:
    ''' The SudokuSolver class has 10 functions:

    __init__                        : instantiates SudokuSolver class
    convert                         : converts the input string into our 2-dimensional game board format
    board                           : prints out the board
    done                            : checks our_board to see if there are any remaining zeros on the board
    solve                           : performs steps required to fill the Sudoku board
    rules_based_element_elimination : fills in our_board & possibilities
    possible_numbers                : returns potential numbers in a Sudoku board
    get_box_boundaries              : returns the boundaries of a box
    row_with_min_guessing           : returns row with the fewest blanks and associated possible solutions for the row
    result                          : returns solved board in str-format (used for unittest)
    '''

    def __init__(self, board_string):
        ''' This function instantiates SudokuSolver class.
            It will call convert() on our board_string.

            Arguments:
            board_string(string):   string of numbers to populate our board

            Returns:
            none
        '''

        self.our_board = self.convert(board_string)  # global class 2d-list
        self.possibilities = [ele[:] for ele in self.our_board] # creates a copy of our board for updating possibilities


    def convert(self, board_string):
        ''' This function converts the input string into our 2-dimensional game board format.

        Arguments:
        board_string(string):   string of numbers to populate our Sudoku board

        Returns:
        converted_board(list):  a 9x9-list of lists that represent our board
        '''

        converted_board = []  # local variable to house our converted board

        # for loop to iterate through our entire string
        for rows in range(0, 81, 9):
            # append board rows to converted_board list (this makes a list of lists of ints)
            converted_board.append([int(index) for index in board_string[rows:rows+9]])

        return converted_board  # return our converted board


    def board(self):
        ''' This function will print out the board.

            Arguments:
            none

            Returns:
            none
        '''

        answer = ''  # our answer string used for output

        # for loop to print out our board
        for row in range(0, 9):
            # print a divider in the appropriate places
            if(row == 0 or row == 3 or row == 6):
                answer += '---------------------\n'
            answer += f'{" ".join(map(str, self.our_board[row][0:3]))} | {" ".join(map(str, self.our_board[row][3:6]))} | {" ".join(map(str, self.our_board[row][6:9]))}\n'
        answer += '---------------------\n'

        return answer  # return our answer


    def done(self):
        ''' This function checks our_board to see if there are any remaining zeros on the board.
        If there are zeros, we return "False" since there are still unsolved squares.  If
        there aren't any zeros, we return "True."

        Arguments:
        none

        Returns:
        False(bool):   if board is not complete
        True(bool):    if board is complete
        '''

        for row in range(0, 9):  # loop through each of the rows
            for col in range(0, 9):  # loop through each of the elements
                if(self.our_board[row][col] == 0):  # if any element on the board is a zero
                    return False  # we return False since the board is not complete

        return True  # if we didn't return False above, then we're done so "True" is returned


    def solve(self):
        ''' This function will perform the steps required to fill the Sudoku board.

        Arguments:
        none

        Returns:
        True(bool):    if this method is done
        False(bool):   if this method is not done
        '''

        self.rules_based_element_elimination()  # run the rules_based_element_elimination algorithm to fill in squares

        if(self.done() == True):  # if there are no zeros remaining
            return True # Congrats - we've solved the board!

        else:  # otherwise, we're not done so we:
            row_min, row_possibles = self.row_with_min_guessing()  # get a row's element w/minimum amount of guesses

            for current_row in row_possibles:  # loop through all the rows in the possibles list
                confirmed_board = [ele[:] for ele in self.our_board]  # make a deep-copy of our board before making guesses
                confirmed_possibilities = [ele[:] for ele in self.possibilities] # make deep copy of possibilities board for rollback
                self.our_board[row_min] = current_row  # set the element @ certain row to our number from row possibles
                self.possibilities[row_min] = current_row # updates possibilities board

                done = self.solve()  # <---- recursion call done here

                if(done == True):  # if we've returned True (from the first if-statement) in the function
                    return True  # we are done!

                elif(done == False):  # if the board hasn't been solved
                    self.our_board = [ele[:] for ele in confirmed_board]  # reload the last known good-board and try again
                    self.possibilities = [ele[:] for ele in confirmed_possibilities] # reload the last known good possibilities matrix

            return False  # We're not done yet


    def rules_based_element_elimination(self):
        ''' This function will fill in our_board[rox][column] with answers with one possibility.
        If our_board[row][column] has more than one possibility, it will fill possibilities[row][column]
        with a list of possibles.

        Arguments:
        none

        Returns:
        none
        '''

        update_made = True  # set this to True (just to get us in the while-loop below)

        while(update_made == True):  # keep running while true
            update_made = False # reset this to false

            for row in range(0, 9):  # for-loop to iterate through the entire row
                for column in range(0, 9):  # for-loop to iterate through each column
                    possibles = self.possible_numbers(row, column)  # get a list of possible numbers for the coord

                    if(possibles == False):  # this means we've already locked in the number
                        continue  # so, we continue on to the next number

                    if(len(possibles) == 1):  # if there's only 1 possible, then we lock that in-place
                        self.our_board[row][column] = possibles[0]  # lock-in our number for that row/column
                        self.possibilities[row][column] = possibles[0] # changes result from single element array to value
                        update_made = True  # we made an update, so keep us in the loop

                    else:
                        self.possibilities[row][column] = possibles # updates the board with possibilities

            if(update_made == False):  # if no updates are made
                return  # return


    def possible_numbers(self, row, column):
        ''' This function will identify potential numbers in a Sudoku board by
        checking each row, column, and box for numbers already locked-in.

        Arguments:
        row(int):           x-coordinate of element
        column(int):        y-coordinate of element

        Returns:
        False(bool):        return False if we've locked in the number
        all_numbers(list):  list of possible numbers not seen in row, col, or box
        '''

        if(self.our_board[row][column] != 0):  # if a number has already been locked-in
            return False  # no need to modify it

        # create a list of all numbers in the Sudoku board to check for
        all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for numbers in self.our_board[row]:  # check the entire row
            if(numbers in all_numbers):  # if that number is in that row
                all_numbers.remove(numbers)  # we remove it from our 'all_numbers' list

        for numbers in range(0, 9):  # now, we check the entire column
            if(self.our_board[numbers][column] in all_numbers):  # if that number is in that column
                all_numbers.remove(self.our_board[numbers][column])  # we remove it from our all_numbers list

        x_start, x_end, y_start, y_end = self.get_box_boundaries(row, column)  # get box boundaries for coordinate in question

        box = self.our_board[x_start: x_end]   # get the rows value for our box --> 3x9-list of lists at this point

        for index, value in enumerate(box):  # enumerate this, so we can get the index and values for the row
            box[index] = value[y_start: y_end]  # slicing gives us numbers within our corresponding box ---> 3x3-list of lists

        for row in range(0, 3):  # loop through each of our rows in the box we just made
            for col in range(0, 3):  # loop through the elements in the corresponding box
                if(box[row][col] in all_numbers):  # if the number we're on is seen in our all_numbers list
                    all_numbers.remove(box[row][col])  # we remove that number from our all_numbers list

        return all_numbers  # return a list of numbers that haven't been seen in the row, column, or box


    def get_box_boundaries(self, row, column):
        ''' This function will return the boundaries of a box.
        This will be used to search for numbers within the box.

        Arguments:
        row(int):          x-coordinate of the value
        column(int):       y-coordinate of the value

        Returns:
        row_start(int):    x-coordinate start of box
        row_end(int):      x-coordinate end of box
        col_start(int):    y-coordinate start of box
        col_end(int):      y-coordinate end of box

        '''

        row_start = 0  # variable for our start x_coordinate
        col_start = 0  # variable for our start y_coordinate

        if(row < 2):  # if our row is less than 3
            row_start = 0  # we start at 0 element

        elif(row >= 3 and row < 6):  # if our row is 3-5
            row_start = 3  # we start at element 3

        elif(row >= 6):  # if our row is 6 or greater
            row_start = 6  # we start at 6

        if(column < 2):  # if our column is less than 3
            col_start = 0  # we start at 0 element

        elif(column >= 3 and column < 6):  # if our column is 3-5
            col_start = 3  # we start at element 3

        elif(column >= 6):  # if our column is 6 or greater
            col_start = 6  # we start at 6

        row_end = row_start + 3  # end for row now complete
        col_end = col_start + 3  # end for col now complete

        # return the box boundaries for our possible_numbers function
        return row_start, row_end, col_start, col_end


    def row_with_min_guessing(self):
        ''' This method returns the row with the fewest blanks and associated possible solutions for the row. Method is used in the solve function to make a guess for a whole row rather than a single element.

        Arguments:
        none

        Returns:
        min_row_index(int):             index for the row with the fewest blanks
        possible_row_solutions(list):   list of possible solutions of for that row
        '''

        min_zero_row_indexes = list(range(9))  # largest possible list to compare against
        min_row_index = 0  # initialize the row index
        min_possibles_elements = []  # list to store possible elements

        # iterate across each row in the possibilities matrix
        for i, row in enumerate(self.possibilities):
            zeros_row = [] # initializes zeros index list
            possibles_row = [] # initialize element list, corresponds to zeros row

            # iterate across each element in the possibilities matrix row
            for j, elem in enumerate(row):
                if type(elem) is list: # check to make sure the element is a list
                    zeros_row.append([i,j]) # add the index to the stack
                    possibles_row.append(elem) # add the element to the stack

            if len(zeros_row) > 0 and len(zeros_row) < len(min_zero_row_indexes): # check if stack is shorter than previous min stack
                min_zero_row_indexes = zeros_row  # update values
                min_row_index = i  # set min_row_index to current index of row
                min_possibles_elements = possibles_row  # set min_possibles_elements to our possibles_row list

        possible_row_solutions = [] # initialize resulting solution

        # iterate across each element whichs creates all combinations of the arrays fed in (equivalent to nested for loops)
        for row in list(itertools.product(*min_possibles_elements)):
            if len(set(row)) == len(row): # filters combinations with repeated elements/ yields only unique number combinations
                new_row = [ele for ele in self.possibilities[min_row_index]] # copy row to keep non-zero values
                for entry, index in zip(row, min_zero_row_indexes): # loop through entries and their corresponding indices
                    new_row[index[1]] = entry # update new row only at the spot where a guess is being made
                possible_row_solutions.append(new_row) # adds complete 9 item row to possible list

        return min_row_index, possible_row_solutions  # return row with min possibilities & possible row solutions


    def result(self):
        ''' This function is used for unittest.

        Arguments:
        none

        Returns:
        string(string):  81-character string representation of our_board after being solved

        '''

        self.solve()  # solve our board

        # flatten our_board (9x9-list of ints) into a 1x81 string (since we can't compare digits of 81-length)
        result = [str(item) for self.our_board in self.our_board for item in self.our_board]

        return ''.join(result)  # return our board as a string so we can compare



# ------------------------------------------------------------------------------
#                             Driver Code Below
# ------------------------------------------------------------------------------
game = []  # blank list which will store all the Sudoku boards from our CSV file
# Open the 50x Sudoku challenges csv-file
with open('sample_sudoku_board_inputs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:  # for each row in our Sudoku challenges file
        game.append(row)  # add that to our list
for board_nbr in range(0, len(game)):  # we're going to solve all the boards we just read
    game[board_nbr] = ''.join(game[board_nbr])
    current_board = SudokuSolver(game[board_nbr])  # instantiate a class instance for the board
    current_board.solve()  # solve our current board
    print(f'Board Number: {board_nbr+1}\n')  # print our current board number
    print(current_board.board())  # print the solved board

