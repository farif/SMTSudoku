'''
Created on Jul 10, 2020

@author: marif
'''

class PuzzleEncoder:
    
    def __init__(self, _SIZE, _grid,):
        
        self.BLOCK_SIZE = 3
        self.PUZZLE_SIZE = 9
         
        self.puzzle_grid = _grid 
        

    def entry(self, row,col):
        return "x%d%d" % (row, col)
    
    def declare_entry(self, r, c):
        
        puzzle = []
        
        e = self.entry(r + 1, c + 1)
        puzzle.append("(declare-const %s Int)" % e)
        #sy = Symbol("%s"%(e), INT)
        
        
        _entry = self.puzzle_grid[r][c]
        if _entry == ".":
            puzzle.append("(assert (<=  1 %s 9))" % e)
    #        puzzle.append("(assert (<= %s 9))" % e)
    #        symbolic_puzzle.append(sy >= 1)
    #        symbolic_puzzle.append(sy <= 1)
        else:
            puzzle.append("(assert (= %s %s))" % (e, _entry))
            
        return '\n'.join(map(str, puzzle))
    
    def block_constraints(self, n):
        
        sudoku_instance = []
        for i in range(0, n):
            for c in range(1, n):
                a1 = '(assert (Block %s %s))'%(i*n+c,i*n+(c+1))
                a2 = '(assert(not (Block %s %s)))'%((c-1)*n+1, (c*n)+1)
                if not a1 in sudoku_instance:
                    sudoku_instance.append(a1) 
                if not a2 in sudoku_instance:
                    sudoku_instance.append(a2)
                
        return '\n'.join(sudoku_instance)        
    
    ## Entry point.
    def prepare_encoding(self):
        
        puzzle_encoding = []
        
        puzzle_encoding.append(self.block_constraints(self.BLOCK_SIZE))
        for r in range(self.PUZZLE_SIZE):
            for c in range(self.PUZZLE_SIZE):    
    #    print(r, puzzle_grid[r])
                puzzle_encoding.append(self.declare_entry(r, c))
                
        puzzle_encoding.append("(assert (and ") 
        for r in range(self.PUZZLE_SIZE):
            for c in range (self.PUZZLE_SIZE):
                _entry = self.puzzle_grid[r][c]
                if _entry == '.':
                    v = "x%d%d"%(r+1,c+1)
                    puzzle_encoding.append("(= (S %d %d) %s)"%(r+1,c+1,v))
                else:
                    puzzle_encoding.append("(= (S %d %d) %s)"%(r+1,c+1,_entry))
        puzzle_encoding.append("))")
        
    #    print('\n'.join(map(str, puzzle_encoding)))
        return puzzle_encoding
    
    def get_values(self):
        
        values = []
        
        values.append("(check-sat)")
#        values.append("(get-model)")
        
        for r in range(self.PUZZLE_SIZE):
            for c in range (self.PUZZLE_SIZE):
                _entry = self.puzzle_grid[r][c]
                if _entry == '.':
                    v = "x%d%d"%(r+1,c+1)
                    values.append("(get-value (%s))"%(v))
                    
        return '\n'.join(map(str, values))            
