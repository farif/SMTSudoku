'''
Created on Jul 10, 2020

@author: marif
'''

from edu.uiowa.encoder.SMTEncoder import *
from edu.uiowa.encoder.SudokuLib import *


class SudokuSolver:

    def __init__(self, _puzzle_grid):
        B_SIZE = 3
        self.p_encoder = PuzzleEncoder(B_SIZE, _puzzle_grid)


    def encode_puzzle(self):    
        puzzle_encoding = self.p_encoder.prepare_encoding()
        puzzle_constraints = '\n'.join(map(str, puzzle_encoding))

        puzzle_constraints = Sudoku_SMT_Lib + puzzle_constraints + self.p_encoder.get_values()
    
        return puzzle_constraints
    
#    def solve(self):    
#        continue