from table import Table
from run import Run
import sys

'''
    This file will be called upon running the Robot Challenge task
    The required files like creating the table, intercepting the commands will all automatically be run.
'''

# try creating a table for now
# 
def main():
    '''
        Unused--- this was only for testing purposes
    '''
    _table = Table()

def ytb():
    program = Run()
    
    for command in sys.stdin:
        program.run(command)


if __name__ == "__main__":
    ytb()




