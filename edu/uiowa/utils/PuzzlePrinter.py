'''
Created on Jul 10, 2020

@author: marif
'''
import re

PUZZLE_SIZE = 9
BLOCK_SIZE = 3

regex_one_entry = "\\s*([1-9\\.])\\s*"
regex_one_line = ""

for i in range(9):
    regex_one_line += regex_one_entry

re_line = re.compile(regex_one_line)

def parse_sudoku_line(line):
    match_line = re_line.search(line)
    if match_line:
        entries = []
        for i in range(PUZZLE_SIZE):
            entries.append(match_line.group(i + 1))
        return entries
    else:
        raise Exception("Invalid input line '{0}'.".format(line))
    
def read_puzzle(puzzle):
    puzzle_grid = []
    
    with open(puzzle) as fp:
        line = fp.readline()
        cnt = 1        
        while line:
#            print("{}".format(line.strip()))
            grid_line = parse_sudoku_line(line)
            puzzle_grid.append(grid_line)
            line = fp.readline()                            
            cnt += 1    
    return puzzle_grid

    
def print_sudoku(board):
    
    print(';',"-"*35)
    for i, row in enumerate(board):
        print((";|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print(';',"-"*35)
        elif i % 3 == 2:
            print(";|" + "---+"*8 + "---|")
        else:
            print(";|" + "   +"*8 + "   |")
            
def pp_result(result, p_grid):
    
    for r in result:
        r = r.replace('(','')
        r = r.replace(')','')
        v_pair =  r.split()
        
        (r,c) = (int(v_pair[0][1])-1, int(v_pair[0][2])-1)
        
        p_grid[r][c] = v_pair[1]
         
    return p_grid    
        
        
#def pretty_print(puzzle_grid):
#    return '\n'.join(['.'.join([c for c in line]) for line in puzzle_grid])
            