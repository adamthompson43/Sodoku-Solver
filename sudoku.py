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
root.geometry("700x700")

entries = []


for x in range(9):
    for y in range(9):
        entry =Text(root, width=2, height=1, font="Calibri 40")
        entry.grid(row = x, column=y)
        entries.append(entry)



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
calculate = Button(root, text= "Solve", command=solve )
calculate.grid(row=10, column=4)
root.mainloop
solve()