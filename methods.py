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
   
    def naked_subset_rows(self):
        for row in self.rows:
            compare_values, delete_values,compare_values_3 = [],[],[]
            for column in self.columns:
                if len(self.board[f'{column}{row}']) == 1:
                    continue
                if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 2:
                    delete_values.append(self.board[f'{column}{row}'])
                    continue

                if self.board[f'{column}{row}'] in compare_values and self.board[f'{column}{row}'] in compare_values_3:
                        delete_values.append(self.board[f'{column}{row}'])
                if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 3:
                    compare_values_3.append(self.board[f'{column}{row}'])
                    continue
                
                compare_values.append(self.board[f'{column}{row}'])
            for column in self.columns:
                for nested_list in delete_values:
                    if nested_list ==  self.board[f'{column}{row}']:
                        continue
                    else:
                        for entry in nested_list:
                            if entry in self.board[f'{column}{row}']:
                                self.board[f'{column}{row}'].remove(entry)

    def naked_subset_columns(self):
        for column in self.columns:
            compare_values, delete_values,compare_values_3 = [],[],[]
            for row in self.rows:
                if len(self.board[f'{column}{row}']) == 1:
                    continue
                if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 2:
                    delete_values.append(self.board[f'{column}{row}'])
                    continue

                if self.board[f'{column}{row}'] in compare_values and self.board[f'{column}{row}'] in compare_values_3:
                        delete_values.append(self.board[f'{column}{row}'])
                if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 3:
                    compare_values_3.append(self.board[f'{column}{row}'])
                    continue
                
                compare_values.append(self.board[f'{column}{row}'])
            for row in self.rows:
                for nested_list in delete_values:
                    if nested_list ==  self.board[f'{column}{row}']:
                        continue
                    else:
                        for entry in nested_list:
                            if entry in self.board[f'{column}{row}']:
                                self.board[f'{column}{row}'].remove(entry)

    def naked_subset_box(self):
        for quadrant in range(1,10):
            compare_values, delete_values,compare_values_3 = [],[],[]
            for column in self.quadrants[f'{quadrant}'][0]:
                for row in self.quadrants[f'{quadrant}'][1]:
                    if len(self.board[f'{column}{row}']) == 1:
                        continue
                    if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 2:
                        delete_values.append(self.board[f'{column}{row}'])
                        continue

                    if self.board[f'{column}{row}'] in compare_values and self.board[f'{column}{row}'] in compare_values_3:
                        delete_values.append(self.board[f'{column}{row}'])
                    if self.board[f'{column}{row}'] in compare_values and len(self.board[f'{column}{row}']) == 3:
                        compare_values_3.append(self.board[f'{column}{row}'])
                        continue


                    compare_values.append(self.board[f'{column}{row}'])
            for column in self.quadrants[f'{quadrant}'][0]:
                for row in self.quadrants[f'{quadrant}'][1]:
                    for nested_list in delete_values:
                        if nested_list ==  self.board[f'{column}{row}']:
                            continue
                        else:
                            for entry in nested_list:
                                if entry in self.board[f'{column}{row}']:
                                    self.board[f'{column}{row}'].remove(entry)

    def hidden_subset_rows(self):
        for row in self.rows:
            count = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            compare_values,values_at_2 = [],[]
            for column in self.columns:
                compare_values.append([self.board[f'{column}{row}'],f'{column}{row}'])
            for values in compare_values:
                for value in values[0]:
                    count[f'{value}'] += 1

            for count_iterator in range(1,10):
                if count[f'{count_iterator}'] == 1:
                    for value in compare_values:
                        if count_iterator in value[0]:
                            self.board[value[1]] = [count_iterator]
                
                if count[f'{count_iterator}'] == 2:
                    values_at_2.append(str(count_iterator))

            
            if len(values_at_2) >= 2:
                counter = 1
                combos = []
                for x in values_at_2[0:-1]:
                    for y in values_at_2[counter:]:
                        if x != y:
                            combos.append([int(x),int(y)])
                    counter += 1
                
                for x in combos:
                    hold =[]
                    for values in compare_values:
                        if x[0] in values[0] and x[1]in values[0]:
                            hold.append(values[1])
                    if len(hold) == 2:
                        for square in hold:
                            self.board[square] = [int(x[0]),int(x[1])]

    def hidden_subset_columns(self):
        for column in self.columns:
            count = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            compare_values,values_at_2 = [], []
            for row in self.rows:
                compare_values.append([self.board[f'{column}{row}'],f'{column}{row}'])
            for values in compare_values:
                for value in values[0]:
                    count[f'{value}'] += 1

            for count_iterator in range(1,10):
                if count[f'{count_iterator}'] == 1:
                    for value in compare_values:
                        if count_iterator in value[0]:
                            self.board[value[1]] = [count_iterator]

                if count[f'{count_iterator}'] == 2:
                    values_at_2.append(str(count_iterator))

            
            if len(values_at_2) >= 2:
                counter = 1
                combos = []
                for x in values_at_2[0:-1]:
                    for y in values_at_2[counter:]:
                        if x != y:
                            combos.append([int(x),int(y)])
                    counter += 1
                
                for x in combos:
                    hold =[]
                    for values in compare_values:
                        if x[0] in values[0] and x[1]in values[0]:
                            hold.append(values[1])
                    if len(hold) == 2:
                        for square in hold:
                            self.board[square] = [int(x[0]),int(x[1])]

    def hidden_subset_box(self):
        for quadrant in range(1,10):
            compare_values, values_at_2 = [], []
            count = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for column in self.quadrants[f'{quadrant}'][0]:
                for row in self.quadrants[f'{quadrant}'][1]:
                    compare_values.append([self.board[f'{column}{row}'],f'{column}{row}'])
                for values in compare_values:
                    for value in values[0]:
                        count[f'{value}'] += 1

            for count_iterator in range(1,10):
                if count[f'{count_iterator}'] == 1:
                    for value in compare_values:
                        if count_iterator in value[0]:
                            self.board[value[1]] = [count_iterator]
                            break

                if count[f'{count_iterator}'] == 2:
                    values_at_2.append(str(count_iterator))

            
            if len(values_at_2) >= 2:
                counter = 1
                combos = []
                for x in values_at_2[0:-1]:
                    for y in values_at_2[counter:]:
                        if x != y:
                            combos.append([int(x),int(y)])
                    counter += 1
                
                for x in combos:
                    hold =[]
                    for values in compare_values:
                        if x[0] in values[0] and x[1]in values[0]:
                            hold.append(values[1])
                    if len(hold) == 2:
                        for square in hold:
                            self.board[square] = [int(x[0]),int(x[1])]

                

    


            #     if count[f'{count_iterator}'] == 2:
            #         values_at_2.append(str(count_iterator))
            # for x in values_at_2:
            #     for values in compare_values:
            #         if x in values[0]:

            # for column in self.columns:
            #     for nested_list in delete_values:
            #         if nested_list ==  self.board[f'{column}{row}']:
            #             continue
            #         else:
            #             for entry in nested_list:
            #                 if entry in self.board[f'{column}{row}']:
            #                     self.board[f'{column}{row}'].remove(entry)

    def x_wing_row(self):
        for check_number in range(1,10):
            possible_squares= []
            for row in self.rows:
                hold = []
                count = 0
                for column in self.columns:
                    if check_number in self.board[f'{column}{row}']:
                        hold.append(f'{column}{row}')
                        count += 1
                if count == 2:
                    possible_squares.append(hold)
            if len(possible_squares) >= 2:
                iteration_count = 1
                for x in possible_squares[0:-1]:
                    for y in possible_squares[iteration_count:]:
                        iteration_count += 1
                        if x[0][0]==y[0][0] and x[1][0]==y[1][0] and x[0][1]==x[1][1] and y[0][1]==y[1][1]:
                            for z in range(1,10):
                                if z != int(x[0][1]) and z != int(y[0][1]):
                                    if check_number in self.board[f'{x[0][0]}{z}']:
                                        self.board[f'{x[0][0]}{z}'].remove(check_number)
                                    if check_number in self.board[f'{x[1][0]}{z}']:
                                        self.board[f'{x[1][0]}{z}'].remove(check_number)

    def x_wing_column(self):
        for check_number in range(1,10):
            possible_squares= []
            for column in self.columns:
                hold = []
                count = 0
                for row in self.rows:
                    if check_number in self.board[f'{column}{row}']:
                        hold.append(f'{column}{row}')
                        count += 1
                if count == 2:
                    possible_squares.append(hold)
            if len(possible_squares) >= 2:
                iteration_count = 1
                for x in possible_squares[0:-1]:
                    for y in possible_squares[iteration_count:]:
                        iteration_count += 1
                        if x[0][0]==y[0][0] and x[1][0]==y[1][0] and x[0][1]==x[1][1] and y[0][1]==y[1][1]:
                            for z in self.columns:
                                if z != x[0][0] and z != x[1][0]:
                                    if check_number in self.board[f'{z}{x[0][1]}']:
                                        self.board[f'{z}{x[0][1]}'].remove(check_number)
                                    if check_number in self.board[f'{z}{y[0][1]}']:
                                        self.board[f'{z}{y[0][1]}'].remove(check_number)

    def swordfish(self):
        for check_number in range(1,10):
            p_sq= []
            for row in self.rows:
                hold = []
                count = 0
                for column in self.columns:
                    if check_number in self.board[f'{column}{row}']:
                        hold.append(f'{column}{row}')
                        count += 1
                if count == 2:
                    p_sq.append(hold)
            if len(p_sq) == 4:
                chk =[p_sq[0][0][0],p_sq[1][0][0],p_sq[2][0][0],p_sq[3][0][0], p_sq[0][1][0],p_sq[1][1][0],p_sq[2][1][0],p_sq[3][1][0]]
                if chk[0]==chk[1] and chk[2]==chk[3] and chk[4]==chk[5] and chk[6]==chk[7]:
                    for x in p_sq:
                        for column2 in self.columns:
                            if x[0][0] != column2 and x[1][0] != column2:
                                if check_number in self.board[f'{column2}{x[0][1]}']:
                                    self.board[f'{column2}{x[0][1]}'].remove(check_number)








    
            
            
            
            



