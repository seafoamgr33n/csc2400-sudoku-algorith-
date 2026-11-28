from sudokugrid import sudoku
import time 

# a greedy algorithm takes the first possible workable number.

def greedySudoku(grid):

    # probably use recursion because i thought of storing
    # nums and coords in a stack but then i was like what am i doing
    # it should stop at the last cell, bottom right, after iterating through row cells
    # x is like if you flipped the matrix its left side. literally counting rows
    
    x, y = grid.find_open()

    if x == "end":
        return "advance"

    for num in range (1, 10):
        # iterate through possibilities, 
        # take the first that works.
        # use the recursive stack to store stuff. 
        # if something is safe, we advance. 
        if grid.is_valid_all(num, x, y):
            grid.grid[x][y] = num
            if greedySudoku(grid) == "advance":
                return "advance"
            # if NOTHING works we have to reset
            grid.grid[x][y] = 0 


    return "backtrack"

def main():
    
    grid = sudoku(1)
    start = time.time() # starting time
    greedySudoku(grid)  # run the algorithm
    end = time.time()   # ending time
    print(f"for unfilled grid: {end - start:.5f} seconds") # show how long it took

    grid2 = sudoku('src/third_algorithm/sudoku.json')
    start = time.time() # see how long thd algorighm takes
    greedySudoku(grid2)
    end = time.time()
    print(f"for filled grid: {end - start:.3f} seconds")

    grid.printgrid()
    grid2.printgrid()

if __name__ == "__main__":
    main()
