from sudokugrid import sudoku

# a greedy algorithm takes the first possible workable number.

def greedySudoku(grid, xi, yi):

    # probably use recursion because i thought of storing
    # nums and coords in a stack but then i was like what am i doing
    # it should stop at the last cell, bottom right, after iterating through row cells
    
    x = xi
    y = yi

    if x == 9 and y == 8:
        return "advance" # base case for when we are done

    # take care of occupied squares if we're inputting data
    while grid[xi][yi] != 0:
        x = x + 1
        if x == 9:
            y += 1
            x = 0

    for num in range (1, 10):
        # iterate through possibilities, take the first that works.
        # use the recursive stack to store stuff. 
        # if something is safe, we advance. 
        if grid.is_valid_all:
            grid[x][y] = num
            if greedySudoku(grid, x, y+1) == "advance":
                return "advance"
            # if NOTHING works we have to reset
            grid[x][y] = 0 


        return "backtrack"

    

def main():
    grid = sudoku()
    greedySudoku(grid, 0,0)
    print(grid)


