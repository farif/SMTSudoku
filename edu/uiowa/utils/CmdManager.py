'''
Created on Jul 10, 2020

@author: marif
'''

import subprocess
import os
from os import system, name 

def run_cvc4(smt_def):
    smt_tmp = 'def_file.smt2'
    smt_file = open(smt_tmp, 'w')
    
    smt_file.write(smt_def)
    
    smt2_file_path = os.path.abspath(smt_file.name)
    
    smt_file.flush()
    smt_file.close()
    
#    print("SMT File PATH:", smt2_file_path)
    
    solver_path = os.path.abspath('lib/cvc4')
      
    #--no-sygus-eval-agg-cache
    cmd = solver_path + ' ' + smt2_file_path
    
#    cmd = 'ls -al'
    cmd = list(cmd.split(' '))
    
    result = run_cmd(cmd)
    
    return result

def run_cmd(cmd):
    
#    start = 
    result = []
        
    EOF = 'unknown\n'
    #Timeout
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        #buffer = []
        for line in process.stdout:
            #buffer.append(str(line))
            
            read_data = line.decode()

            if EOF in read_data:
                continue
            else:#adt_type
                result.append(read_data)
                
    except Exception as e:
#        logging.warn('Unable to Run CVC4...')
        print(str(e))
#        exit
#    outfile.close    

    return result    

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 