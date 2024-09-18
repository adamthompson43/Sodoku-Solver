import numpy as np
from tkinter import *

grid = [[9,0,0,0,2,0,1,0,0],
        [0,8,0,0,0,0,9,6,0],
        [6,0,0,0,0,0,0,0,0],
        [4,0,8,0,0,2,0,0,0],
        [0,0,3,0,0,8,0,0,0],
        [0,0,0,6,1,9,0,0,0],
        [0,7,5,0,0,0,0,0,4],
        [0,0,0,1,0,0,0,0,2],
        [0,0,0,0,7,0,0,8,0]]

# window!
root = Tk()
root.title("Sudoku Solver")
root.geometry("500x500")
entry0_0 = Entry(root)
entry0_1 = Entry(root)

entry0_0.grid(row = 0, column = 0, pady = 2)
entry0_1.grid(row = 0, column = 1, pady = 2)

# for x in range(0:10)
#     for y in range(0:10)
#     entry


def possible(row, column, number):
    global grid 

    # check if number appears in row
    for i in range(0,9):
        if grid[row][i] == number:
            return False
        
    # check if number appears in column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
        
    # check if number appears in box
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return
      
    print(np.matrix(grid))
    input('[Enter] More possible solutions')

root.mainloop
solve()