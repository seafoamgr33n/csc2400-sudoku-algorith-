#brute force algorithm
#uses a 1 dimensional list instead of a grid bc it makes it much faster
import math

#I test it on a 4x4 grid bc the 9x9 is too big
EDGE_LENGTH= 4 #4 or 9
BOX_LENGTH= 2 #2 or 3
BOARD_SIZE = 16 #16 or 81
empty_cells = []


class SudokuBoard:
    def __init__(self):
        #make the sudoku grid
        #self.board = [0]*BOARD_SIZE
        self.board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.counter = 0
        #perfect board
        #self.board = [1,2,3,4,3,4,1,2,2,1,4,3,4,3,2,1]

    def set_value(self,i,value):
        self.board[i] = value

    def get_row(self,row_index):
        row = []
        spot_to_check = row_index*EDGE_LENGTH
        for i in range(EDGE_LENGTH):
            row.append(self.board[spot_to_check])
            spot_to_check += 1
        return row


    def get_column(self,col_index):
        col=[]
        spot_to_check = col_index
        for i in range(EDGE_LENGTH):
            col.append(self.board[spot_to_check])
            spot_to_check += EDGE_LENGTH
        return col

    def get_box(self,index):
        box = []

        #get it in 2 dimensions
        row_index = math.floor(index / BOX_LENGTH)
        col_index = (index % BOX_LENGTH)

        #shrinking it down to a box
        var = row_index * (BOX_LENGTH ** BOX_LENGTH)
        box_start = (var + (col_index * BOX_LENGTH))

        position = box_start

        #TODO
        #
        for i in range(BOX_LENGTH):
            for j in range(BOX_LENGTH):
                box.append(self.board[position])
                position += 1
            position = box_start + ((i+1) * (BOX_LENGTH**2))
        return box


    def print_board(self):
        for i in range(EDGE_LENGTH):
            print(self.get_row(i))
        print("\n")

    def set_empty_cells(self):
        for i in range(BOARD_SIZE):
            if self.board[i] == 0:
                empty_cells.append(i)

    # init, set all empty cells to 1
    def init_board(self):
        for i in empty_cells:
            self.set_value(i, 1)

    def reset_cell(self,i):
        self.set_value(i,1)

    #TODO
    #this function being on a 1 dimensional array makes the algorithm much faster
    def add_one(self, i):
        self.set_value(i, self.board[i] + 1)
        self.counter+=1
        if self.counter % 10000 == 0:
            print(self.counter)

    #validate entire grid
    def is_valid(self):

        #check row and column for duplicates
        for i in range(EDGE_LENGTH):
            row=(self.get_row(i))
            #convert it into a set bc sets remove duplicates, then compare lengths
            if len(row) != len(set(row)):
                return False
            col=(self.get_column(i))
            if len(col) != len(set(col)):
                return False
        # check 3x3 box
            box=(self.get_box(i))
            if len(box) != len(set(box)):
                return False

        # if it passes all tests, its valid
        print("IM VALID")
        self.print_board()
        return True

    # add one to first space, if space one is maximum value, defer to next space
    def increment_board(self):
        for i in range(BOARD_SIZE):
            if i in empty_cells:
                if self.board[i] == EDGE_LENGTH:
                    self.reset_cell(i)
                    continue
                else:
                    self.add_one(i)
                    break
        return True

    def brute_force(self):
        # locate all empty cells
        self.set_empty_cells()

        #initialize board
        self.init_board()

        #while the current completed board is not valid, increment bord
        while not self.is_valid():
            self.increment_board()


    def main(self):
        self.brute_force()



if __name__ == '__main__':
    board = SudokuBoard()
    board.main()

