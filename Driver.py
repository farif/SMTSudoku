'''
Created on Jul 10, 2020

@author: marif
'''
from edu.uiowa.utils.PuzzlePrinter import read_puzzle, print_sudoku, pp_result
from edu.uiowa.utils.CmdManager import run_cvc4, clear

from edu.uiowa.sovler.SodokuSolver import SudokuSolver

if __name__ == '__main__':
    puzzle_grid = read_puzzle('/mnt/nfs/clasnetappvm/homedirs/marif/pydev-workspace/SMTLib-Sudoku/puzzles/puzzle1')

    sudoku_solver = SudokuSolver(puzzle_grid)
    sdk_encoding =  sudoku_solver.encode_puzzle()
    
    print_sudoku(puzzle_grid)
    
    print('SMT Solver Running...')    
    result = run_cvc4(sdk_encoding)
    clear() 
    puzzle_grid = pp_result(result, puzzle_grid)
    
    print_sudoku(puzzle_grid)
