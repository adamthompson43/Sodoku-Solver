import numpy as np
from tkinter import *

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

entries = []

def create_grid(root, vcmd):
    """Create the 9x9 grid of entry widgets."""
    global entries
    entries = []
    for x in range(9):
        row_entries = []
        for y in range(9):
            entry = Entry(root, width=2, font="Calibri 40", justify="center")
            entry.grid(row=x, column=y)
            entry.config(validate="key", validatecommand=(vcmd, "%P"))
            row_entries.append(entry)
        entries.append(row_entries)

def validate_input(P):
    if P == "" or (P.isdigit() and 1 <= int(P) <= 9 and len(P) <= 1):
        return True
    return False

def update_grid_from_entries():
    global grid
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            grid[i][j] = int(value) if value != "" else 0

def possible(row, column, number):
    global grid

    if number in grid[row]:
        return False

    for i in range(9):
        if grid[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True

def solve():
    """Solve the Sudoku puzzle."""
    global grid
    update_grid_from_entries() 
    if solve_grid():
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, END)
                entries[i][j].insert(0, str(grid[i][j]))
    else:
        print("No solution exists.")

def solve_grid():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        if solve_grid():
                            return True
                        grid[row][column] = 0

                return False  
    return True  

root = Tk()
root.title("Sudoku Solver")
root.geometry("700x700")

vcmd = (root.register(validate_input), "%P")

create_grid(root, vcmd)

calculate = Button(root, command=solve, text="Solve", font=("Calibri", 20))
calculate.place(x=600, y=600)

root.mainloop()
