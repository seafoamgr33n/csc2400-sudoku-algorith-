#brute force
#each cell is in object in the board object's list

import random
import json

class Board:
    def __init__(self, my_list):
        self.list = my_list
        self.counter = 0
        self.zero_counter = 0
        self.tried_sols_index = 0
        self.empty_cells = []
class Cell:
    def __init__(self, row, col, box, num, my_id):
        self.row = row
        self.col = col
        self.box = box
        self.num = num
        self.id = my_id
        self.tried_sols = []

def init_board():
    #init col row box
    c = 0
    r = 0
    b = 0
    id_counter = 0
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
        with open("sudoku.json","r") as file:           ###for loading in a sudoku puzzle
            data = json.load(file)                      ###
            puzzle = data["puzzle"]                     ###
        cell = Cell(r, c, b, puzzle[r][c], id_counter)  ###

        #cell = Cell(r, c, b, 0,id_counter) ### for generating a random puzzle

        c += 1
        id_counter += 1
        board.list.append(cell)

def set_empty_cells():
    for i in range(81):
        if board.list[i].num == 0:
            board.empty_cells.append(i)

def print_board():
    print()
    for r in range(81):
        if r%9==0 and r!=0:
            print()
        print(board.list[r].num, end=", ")
    print()

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
                    #clear tried sols, set value to 0, and backtrack
                    board.list[new_index].tried_sols.clear()
                    board.list[new_index].num = 0
                    backtracking(new_index)
            else:
                #if it is tried, add to tried sols
                if i not in board.list[new_index].tried_sols:
                    board.list[new_index].tried_sols.append(i)
                #if length of tried sols is 9, clear tried sols, set value to 0, and backtrack
                if len(board.list[new_index].tried_sols) == 9:
                    board.list[new_index].tried_sols.clear()
                    backtracking(new_index)

    return new_index


def brute_force():

    #rand = list(range(1,10))                 ### if generating random board
    #random.shuffle(rand)                     ###
    #print(rand)                              ###
    #for i in range(9):                       ###
    #    if i in empty_cells:                 ###
    #        board.list[i].num = rand[i]      ###
    #i = 9                                    ###

    i = 0         ### if importing board
    while i<81:
        #if cell is empty, iterate numbers till one works
        if i in board.empty_cells:
            for number in range(1,10):
                if is_valid(i,number):
                    board.list[i].num = number
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

    if board.list[80].num != 0:
        print_board()

if __name__ == '__main__':
    board = Board([])
    init_board()
    set_empty_cells()
    brute_force()