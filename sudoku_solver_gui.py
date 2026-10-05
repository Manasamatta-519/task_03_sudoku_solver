import tkinter as tk
from tkinter import messagebox
import random
import copy

SIZE = 9


# ---------------- Sudoku Logic ----------------

def is_valid(grid, row, col, num):
    for c in range(SIZE):
        if grid[row][c] == num:
            return False

    for r in range(SIZE):
        if grid[r][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def find_empty_cell(grid):
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] == 0:
                return row, col
    return None


def solve_sudoku(grid):
    empty = find_empty_cell(grid)

    if empty is None:
        return True

    row, col = empty
    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


def generate_full_solution():
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    solve_sudoku(grid)
    return grid


def generate_puzzle(empty_cells=45):
    solution = generate_full_solution()
    puzzle = copy.deepcopy(solution)

    cells = [(r, c) for r in range(SIZE) for c in range(SIZE)]
    random.shuffle(cells)

    for r, c in cells[:empty_cells]:
        puzzle[r][c] = 0

    return puzzle


# ---------------- GUI Functions ----------------

def set_board(grid, fixed=False):
    for row in range(SIZE):
        for col in range(SIZE):
            entries[row][col].delete(0, tk.END)

            if grid[row][col] != 0:
                entries[row][col].insert(0, str(grid[row][col]))

            if fixed and grid[row][col] != 0:
                entries[row][col].config(
                    fg="#1f4e79",
                    bg="#eaf3ff"
                )
            else:
                entries[row][col].config(
                    fg="black",
                    bg="white"
                )


def new_puzzle():
    puzzle = generate_puzzle(45)
    set_board(puzzle, fixed=True)


def get_grid():
    grid = []

    try:
        for row in range(SIZE):
            current_row = []

            for col in range(SIZE):
                value = entries[row][col].get().strip()

                if value == "":
                    current_row.append(0)
                elif value.isdigit() and 1 <= int(value) <= 9:
                    current_row.append(int(value))
                else:
                    raise ValueError

            grid.append(current_row)

        return grid

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter only numbers from 1 to 9.\n"
            "Leave empty cells blank."
        )
        return None


def solve():
    grid = get_grid()

    if grid is None:
        return

    original = copy.deepcopy(grid)

    if solve_sudoku(grid):
        for row in range(SIZE):
            for col in range(SIZE):
                entries[row][col].delete(0, tk.END)
                entries[row][col].insert(0, str(grid[row][col]))
                entries[row][col].config(
                    fg="#188038",
                    bg="#f0fff0"
                )
    else:
        # Restore the original board if there is no solution.
        set_board(original)
        messagebox.showinfo(
            "No Solution",
            "This Sudoku puzzle has no valid solution."
        )


def clear_board():
    for row in range(SIZE):
        for col in range(SIZE):
            entries[row][col].delete(0, tk.END)
            entries[row][col].config(
                fg="black",
                bg="white"
            )


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Sudoku Solver | Task 03")
root.resizable(False, False)
root.configure(bg="#f4f6f8")

title = tk.Label(
    root,
    text="Sudoku Solver",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8",
    fg="#222222"
)
title.pack(pady=(15, 3))

subtitle = tk.Label(
    root,
    text="Task 03 • Software Development Internship",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#555555"
)
subtitle.pack(pady=(0, 12))

board_frame = tk.Frame(root, bg="#222222", padx=2, pady=2)
board_frame.pack(padx=20, pady=5)

entries = []

for row in range(SIZE):
    row_entries = []

    for col in range(SIZE):
        entry = tk.Entry(
            board_frame,
            width=2,
            font=("Arial", 20, "bold"),
            justify="center",
            bg="white",
            fg="black",
            relief="flat"
        )

        padx = (1, 5) if col % 3 == 2 and col != 8 else (1, 1)
        pady = (1, 5) if row % 3 == 2 and row != 8 else (1, 1)

        entry.grid(
            row=row,
            column=col,
            padx=padx,
            pady=pady,
            ipady=3
        )

        row_entries.append(entry)

    entries.append(row_entries)

button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=15)

new_button = tk.Button(
    button_frame,
    text="New Puzzle",
    command=new_puzzle,
    font=("Arial", 11, "bold"),
    padx=14,
    pady=8
)
new_button.grid(row=0, column=0, padx=5)

solve_button = tk.Button(
    button_frame,
    text="Solve Sudoku",
    command=solve,
    font=("Arial", 11, "bold"),
    padx=14,
    pady=8
)
solve_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_board,
    font=("Arial", 11),
    padx=14,
    pady=8
)
clear_button.grid(row=0, column=2, padx=5)

info = tk.Label(
    root,
    text="New Puzzle generates a different Sudoku each time.",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#666666"
)
info.pack(pady=(0, 15))

# Start with a random puzzle.
new_puzzle()

root.mainloop()
