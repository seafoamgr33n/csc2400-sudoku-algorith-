# brute force algorithm
import itertools

#I test it on a 4x4 grid bc the 9x9 is to big
RANGE_MAX= 4 #4 or 9
BOX_SIZE = 2 #2 or 3

class SudokuBoard:
    def __init__(self):
        #make the sudoku grid
        #self.grid = [[0 for x in range(RANGE_MAX)] for y in range(RANGE_MAX)]
        """
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, ]]
        """
        self.grid = [[0, 0, 0, 0, ],
                     [0, 0, 0, 0, ],
                     [0, 0, 0, 0, ],
                     [0, 0, 0, 0, ]]


    # TODO have player input a grid

    def get_row(self,row_index):
        return self.grid[row_index]

    def get_column(self,col_index):
        cols=[]
        for row in self.grid:
            cols.append(row[col_index])
        return cols

    def set_value(self,x,y,value):
        self.grid[x][y] = value

    def print_grid(self):
        for i in range(RANGE_MAX):
            print(self.get_row(i))
        print()

    #validate entire grid
    def is_valid(self):

        #check row and column for duplicates

        for i in range(RANGE_MAX):
            row_arr=(self.get_row(i))
            if len(row_arr) != len(set(row_arr)):
                return False
            col_arr=(self.get_column(i))
            if len(col_arr) != len(set(col_arr)):
                return False

        # check 3x3 box
        for x in range(0,RANGE_MAX,BOX_SIZE):
            for y in range(0,RANGE_MAX,BOX_SIZE):
                box = [
                    self.grid[x+box_x][y+box_y]
                    for box_x in range(BOX_SIZE)
                    for box_y in range(BOX_SIZE)
                ]
                if len(box) != len(set(box)):
                    return False
        # if it passes all tests, its valid
        return True


    def brute_force(self):
        # locate all empty cells
        all_empty_cells = []
        for x in range(RANGE_MAX):
            for y in range(RANGE_MAX):
                if self.grid[x][y] == 0:
                    all_empty_cells.append((x,y))


        # get all possible combinations
        #make entire grid, then validate, then reset

        #make grid
        var = range(1,RANGE_MAX+1)
        for guess in itertools.product(var, repeat=len(all_empty_cells)):
            for (x,y), value in zip(all_empty_cells, guess):
                self.grid[x][y] = value
                print("adding value")
            #validate
            if self.is_valid():
                print("im valid :)")
                return True
            #reset
            else:
                for (x,y) in all_empty_cells:
                    self.set_value(x,y,0)
                print("ive reset")
        return False



    def main(self):
        self.brute_force()



if __name__ == '__main__':
    grid = SudokuBoard()
    grid.main()



