#brute force
#each cell is in object in the board object's list

import random       ###for randomly generating a puzzle
import json         ###for loading in a puzzle
import time         ###for timing the algorithm

class Board:
    def __init__(self, my_list):
        self.list = my_list
        self.empty_cells = []
class Cell:
    def __init__(self, row, col, box, num, my_id):
        self.row = row
        self.col = col
        self.box = box #3x3
        self.num = num
        self.id = my_id
        self.tried_sols = [] #tried solutions

def init_board():
    #init col row box
    c = 0
    r = 0
    b = 0
    id_counter = 0

    with open("sudoku.json", "r") as file:  ###for loading in a puzzle
        data = json.load(file)              ###
        puzzle = data["puzzle_266"]             ###

        #standard puzzle = puzzle
        #hard puzzle = puzzle_266

    for i in range(81):
        if c == 9:
            r += 1
            c = 0
        match (r,c):
            case (d,e) if 0<=d<=2 and 0<=e<=2:
                b=0
            case (d,e) if 0<=d<=2 and 3<=e<=5:
                b=1
            case (d,e) if 0<=d<=2 and 6<=e<=8:
                b=2
            case (d,e) if 3<=d<=5 and 0<=e<=2:
                b=3
            case (d,e) if 3<=d<=5 and 3<=e<=5:
                b=4
            case (d,e) if 3<=d<=5 and 6<=e<=8:
                b=5
            case (d,e) if 6<=d<=8 and 0<=e<=2:
                b=6
            case (d,e) if 6<=d<=8 and 3<=e<=5:
                b=7
            case (d,e) if 6<=d<=8 and 6<=e<=8:
                b=8

        cell = Cell(r, c, b, puzzle[r][c], id_counter)  ### for loading in a puzzle

        #cell = Cell(r, c, b, 0,id_counter) ### for randomly generating a puzzle

        c += 1  #have these increment after cell is created but still inside the loop
        id_counter += 1

        board.list.append(cell) #create cell

def set_empty_cells():
    for i in range(81):
        if board.list[i].num == 0:
            board.empty_cells.append(i)

def print_board():
    for r in range(81):
        if r%9==0 and r!=0:
            print()
        print(board.list[r].num, end=", ")
    print("\n")


def is_valid(index,number):
    for i in range(81):
        #check row
        if getattr(board.list[i],"row",None) ==  board.list[index].row:
            if board.list[i].num == number:
                return False
        #check col
        if getattr(board.list[i],"col",None) == board.list[index].col:
            if board.list[i].num == number:
                return False

    box_pos = board.list[index].box #box pos is just a number 0 - 8
    full_box = []
    for i in range(81):
        if board.list[i].box == box_pos:
            full_box.append(board.list[i].id)

    for i in range(9):
        #check box
        #position = box_pos[i]
        if board.list[full_box[i]].num == number:
            return False

    if number == 0:
        return False

    return True


def backtracking(zero_index):
    #zero index is where the value is still zero bc nothing else is valid in that position
    #new index is that position - 1
    new_index=0
    if zero_index >= 1:
        new_index = zero_index-1
    else:
        print("\nerror: index is -1")
        exit(0)
    old_num = board.list[new_index].num  # 1 good
    if old_num not in board.list[new_index].tried_sols:
        board.list[new_index].tried_sols.append(old_num)

    if new_index not in board.empty_cells: #backtrack if it is a set cell
        backtracking(new_index)
    else:
        for i in range(1,10): #values 1-9
            is_tried = False

            #if the current value we are trying has already been tried, dont let it go through
            for t in range(len(board.list[new_index].tried_sols)):
                if i == board.list[new_index].tried_sols[t]:
                    is_tried = True
                    break

            #if value is valid and is not tried, set value
            if is_valid(new_index,i):
                if not is_tried:
                    board.list[new_index].num = i
                    break
                else:
                    continue
            else:
                #if it is tried, add to tried sols
                if i not in board.list[new_index].tried_sols:
                    board.list[new_index].tried_sols.append(i)
                #if length of tried sols is 9, clear tried sols, set value to 0, and backtrack
                if len(board.list[new_index].tried_sols) == 9:
                    board.list[new_index].tried_sols.clear()
                    board.list[new_index].num = 0
                    backtracking(new_index)
    if board.list[new_index].num == 0:
        # clear tried sols and backtrack
        board.list[new_index].tried_sols.clear()
        backtracking(zero_index) #new_index = leaves 0s, zero_index= ???
        #brute_force() #buffered/stuck


    return new_index

def validate_imported_puzzle():
    # check if IMPORTED board is valid
    for i in range(81):
        if i not in board.empty_cells:  # if it is not 0
            value = board.list[i].num  # store the value
            board.list[i].num = 0  # set value to 0
            valid = is_valid(i, value)  # check to see if the stored value is valid
            if valid:
                board.list[i].num = value  # give it back its value
                continue
            else:
                print("\nBoard imported is not valid- error in spot:", i)
                exit(0)

def brute_force():

    #rand = list(range(1,10))                 ### for randomly generating a puzzle
    #random.shuffle(rand)                     ###
    #for i in range(9):                       ###
    #    if i in board.empty_cells:           ###
    #        board.list[i].num = rand[i]      ###


    #i = 9                                    ###

    i = 0         ### for loading in a puzzle
    while i<81:
        #if cell is empty, iterate numbers till one works
        if i in board.empty_cells:
            for number in range(1,10):
                if is_valid(i,number):
                    board.list[i].num = number
                    # print_board()
                    i+=1
                    break
                else:
                    #if it has tried all numbers and value is still 0, backtrack
                    if number == 9:
                        if board.list[i].num ==0:
                            i = backtracking(i)
                            i+=1
        else:
            i+=1
            continue
    for i in range(81):
        if board.list[i].num != 0:
            continue
    print("\nCompleted Board:")
    print_board()
    #exit(0)

if __name__ == '__main__':
    board = Board([])
    init_board()
    set_empty_cells()
    validate_imported_puzzle()

    start = time.time()
    brute_force()
    end = time.time()
    print(f"For imported puzzle: {end - start:.3f} seconds")
    #print(f"For generating a random puzzle: {end - start:.3f} seconds")