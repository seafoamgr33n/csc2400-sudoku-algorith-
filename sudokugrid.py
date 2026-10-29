#create the base sudoku grid
#implement it as a matrix
#subject to changeeeee
#https://www.geeksforgeeks.org/python/python-matrix/ was used for reference.

#TODO create checks for valid cells
    # create check for 3x3 subcells
#TODO create print function

class sudoku: 

    def __init__(self):
        #initialize an empty grid
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0,]]
        #i think it would be fun if we could make a way to format it lol

    #tell us if a choice at a certain loc is valid.
    #that is, if there isn't an identical number on that row. 
    def is_valid_row(self, num, posx, posy):

        #for that row...
        for x in range(10):
            #check every item in the grid
            if self.grid[x][posy] == num:
                #if there's a match it's not valid.
                return False

        #otherwise it is valid.
        return True

    #same as above but for columns
    #it might be easier to combine these into one
    #we'll see
    def is_valid_column(self, num, posx, posy): 
        #for that column...
        for x in range(10):
            #check every item in the column
            if self.grid[posx][x] == num:
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











