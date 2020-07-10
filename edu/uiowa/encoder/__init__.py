
symbolic_puzzle = []

def entry(row,col):
    return "x%d%d" % (row, col)

def declare_entry(r, c):
    
    puzzle = []
    e = entry(r + 1, c + 1)
    puzzle.append("(declare-const %s Int)" % e)
    sy = Symbol("%s"%(e), INT)
    
    
    _entry = puzzle_grid[r][c]
    if _entry == ".":
        puzzle.append("(assert (<=  1 %s 9))" % e)
#        puzzle.append("(assert (<= %s 9))" % e)
#        symbolic_puzzle.append(sy >= 1)
#        symbolic_puzzle.append(sy <= 1)
    else:
        puzzle.append("(assert (= %s %s))" % (e, _entry))
        
    return '\n'.join(map(str, puzzle))

def block_constraints(n):
    
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
def prepare_encoding():
    
    puzzle_encoding = []
    
    puzzle_encoding.append(block_constraints(BLOCK_SIZE))
    for r in range(PUZZLE_SIZE):
        for c in range(PUZZLE_SIZE):    
#    print(r, puzzle_grid[r])
            puzzle_encoding.append(declare_entry(r, c))
            
    puzzle_encoding.append("(assert (and ") 
    for r in range(PUZZLE_SIZE):
        for c in range (PUZZLE_SIZE):
            _entry = puzzle_grid[r][c]
            if _entry == '.':
                v = "x%d%d"%(r+1,c+1)
                puzzle_encoding.append("(= (S %d %d) %s)"%(r+1,c+1,v))
            else:
                puzzle_encoding.append("(= (S %d %d) %s)"%(r+1,c+1,_entry))
    puzzle_encoding.append("))")
    
#    print('\n'.join(map(str, puzzle_encoding)))
    return puzzle_encoding

def get_values():
    values = []
    values.append("(check-sat)")
    values.append("(get-model)")
    for r in range(PUZZLE_SIZE):
        for c in range (PUZZLE_SIZE):
            _entry = puzzle_grid[r][c]
            if _entry == '.':
                v = "x%d%d"%(r+1,c+1)
                values.append("(get-value (%s))"%(v))
                
    return '\n'.join(map(str, values))            
