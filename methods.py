class Methods():
    
    def check_column(self,square):

        if len(self.board[square]) == 1:
            return

        for x in range(1,10):
            if len(self.board[f'{square[0]}{x}']) == 1 and x != int(square[1]):
                if self.board[f'{square[0]}{x}'][0] in self.board[square]:
                    self.board[square].remove(self.board[f'{square[0]}{x}'][0])

    def check_row(self,square):
        if len(self.board[square]) == 1:
            return

        for x in self.columns:
            if len(self.board[f'{x}{square[1]}']) == 1 and x != square[0]:
                if self.board[f'{x}{square[1]}'][0] in self.board[square]:
                    self.board[square].remove(self.board[f'{x}{square[1]}'][0])

    def check_box(self,square):
        if len(self.board[square]) == 1:
            return
        for quadrant in range(1,10):
            if square[0] in self.quadrants[f'{quadrant}'][0] and square[1] in self.quadrants[f'{quadrant}'][1]:
                quadrant_values = []
                for letter in range(0,3):
                    for number in range(0,3):
                        if len(self.board[f"{self.quadrants[f'{quadrant}'][0][letter]}{self.quadrants[f'{quadrant}'][1][number]}"])==1:
                            quadrant_values.append(self.board[f'{self.quadrants[f"{quadrant}"][0][letter]}{self.quadrants[f"{quadrant}"][1][number]}'][0])
                for x in quadrant_values:
                    if x in self.board[square]:
                        self.board[square].remove(x)
   
    def naked_pairs():
        pass