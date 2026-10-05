# Task 03 - Sudoku Solver

## Software Development Internship - SkillCraft Technology

A Python GUI application that generates different Sudoku puzzles and solves them automatically using the Backtracking algorithm.

## Features

- 9x9 graphical Sudoku board
- Generates a new random Sudoku puzzle
- Different puzzle every time
- Automatic Sudoku solving
- Backtracking algorithm
- Manual puzzle input
- Input validation
- Clear button
- No external Python packages required

## Technologies

- Python
- Tkinter
- Recursion
- Backtracking
- Random puzzle generation

## How to Run

```bash
python sudoku_solver_gui.py
```

## How to Use

1. Run the program.
2. A random Sudoku puzzle appears automatically.
3. Click **New Puzzle** to generate another puzzle.
4. Click **Solve Sudoku** to solve the current puzzle.
5. Click **Clear** to empty the board.
6. You can also enter your own Sudoku puzzle manually.

## Algorithm

The application uses backtracking:

1. Find an empty cell.
2. Try numbers from 1 to 9 in random order.
3. Check the row, column, and 3x3 box.
4. Place a valid number.
5. Recursively solve the remaining cells.
6. If a choice fails, undo it and try another number.

## Author

Matta Manasa
