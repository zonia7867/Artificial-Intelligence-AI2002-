# Sudoku Solver

This repository contains a Python Sudoku solver that uses constraint propagation and backtracking search to solve standard 9x9 Sudoku puzzles.

## Files

- `sudoku.py` - main solver script
- `easy.txt` - easy Sudoku puzzle input
- `medium.txt` - medium difficulty Sudoku puzzle input
- `hard.txt` - hard Sudoku puzzle input

## Usage

1. Put your Sudoku puzzle in a text file with exactly 81 characters.
   - Use `0` for blank cells.
   - You may include whitespace or newlines; the script will normalize them.
2. Run the solver:

```bash
python sudoku.py
```

The script reads `easy.txt`, `medium.txt`, and `hard.txt` by default and prints solved grids along with backtracking statistics.

## How it works

- The solver builds a domain of possible digits for every cell.
- It propagates constraints by eliminating values from peers when a cell is assigned.
- It applies hidden single detection within rows, columns, and 3x3 boxes.
- When propagation cannot finish the puzzle, it uses recursive backtracking.

## Adding puzzles

To solve a custom puzzle, add another file in the same folder and update the file list in `sudoku.py` or modify the script to accept command-line input.
