#create the base sudoku grid
#implement it as a matrix
#subject to changeeeee
#https://www.geeksforgeeks.org/python/python-matrix/ was used for reference.

import json

class sudoku: 

    def __init__(self, filepath):
        #initialize an empty grid
        if filepath == 1:
            self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0,]]
        else: 
            with open(filepath, 'r') as file: # load a puzzel!!!!!!!!!!!!!!!!!!!!!
                data = json.load(file)
                self.grid = data["puzzle"]
        
        #i think it would be fun if we could make a way to format it lol

    def printgrid(self):
        for x in range(9): # n,jkgnmhvh,nv
            print(f"{self.grid[x][0]} {self.grid[x][1]} {self.grid[x][2]} {self.grid[x][3]} {self.grid[x][4]} {self.grid[x][5]} {self.grid[x][6]} {self.grid[x][7]} {self.grid[x][8]}")
        print("-----------------")

    #tell us if a choice at a certain loc is valid.
    #that is, if there isn't an identical number on that row. 
    def is_valid_row(self, num, posx, posy):

        #for that row...
        for x in range(9):
            #check every item in the grid
            if self.grid[posx][x] == num:
                #if there's a match it's not valid.
                return False

        #otherwise it is valid.
        return True

    #same as above but for columns
    #it might be easier to combine these into one
    #we'll see
    def is_valid_column(self, num, posx, posy): 
        #for that column...
        for x in range(9):
            #check every item in the column
            if self.grid[x][posy] == num:
                #if there's a match it's not valid.
                return False

        #otherwise it is valid.
        return True

    def is_valid_subgrid(self, num, posx, posy):

        #please don't break

        #for the 3x3 subgrid
        #find a way to anchor our reference point to the upper left of subgrid
        #3 subgrids: for example, a cell on 2,3. 2%3 is 2, so our ref is 0. 
        #same goes for y. ref for 2,3 would be 0,3
        refx = posx - (posx % 3) 
        refy = posy - (posy % 3) 

        #for all x in that subgrid
        for x in range(3):
            #and all y in that subgrid
            for y in range(3):
                if self.grid[refx+x][refy+y] == num:
                    #if there's a match it's not valid.
                    return False

        return True

    def is_valid_all(self, num, x, y): # mash them all together 
        subgrid = self.is_valid_subgrid(num, x, y)  # just test them all
        check2 = self.is_valid_column(num, x, y)         # whatever
        check3 = self.is_valid_row(num, x, y)
        if subgrid == True and check2 == True and check3 == True:
            return True
        return False

    def find_open(self):
        # find the next thingy that is a 0 
        # so we can go in order, filling out a new puzzle
        # or a semi-filled puzzle. 

        # loop through everything
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col

        return "end", "end" # if we're at the base case. 

    def test_quality(self): 
        for x in range(9):        # for every cell
            for y in range(9):    # test if the puzzle is valid
                numb = self.grid[x][y]
                if self.is_valid_all(self, numb, x, y) == False:
                    return "this is not a valid puzzle."

        return "this is a valid puzzle."

        











