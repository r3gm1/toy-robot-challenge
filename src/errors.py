'''
    This file will hold custom error classes 
'''
class OffTableError(Exception):
    '''
        This error will be thrown if the robot attemps to enter a position that is out of boungs
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "SKIPPING: You've attemped to move the Toy Robot off the table" 
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)



class NoCoordinateError(Exception):
    '''
        This error will be raised if a 'move', 'left', 'right'  command is attemped before 
        placing the robot
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "SKIPPING: Please issue the 'PLACE' command before attemping other commands."
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)



class InvalidDirectionError(Exception):
    '''
        This error will be thrown if the direction provided is invalid.
        i.e. it is not within the list
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "SKIPPING: Invalid direction supplied. Valid directions are 'NORTH', 'EAST', 'SOUTH', 'WEST'."
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)



class InvalidPlaceCommandError(Exception):
    '''
        This class will throw an error as the place command wasn't run correctly
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "SKIPPING: Please issue the 'PLACE X,Y,F' command. X,Y are coordinates, and F is a direction."
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)



class CommandNotFoundError(Exception):
    '''
        This is a generic error that is thrown when the command isn't found
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "SKIPPING: Invalid Command. Please issue one of the following commands 'PLACE X,Y,F', 'MOVE', 'LEFT', 'RIGHT', 'REPORT'."
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)




class InvalidIntError(Exception):
    '''
        This error will be thrown if an invalid 'int' is supplied
        i.e. PLACE plp,1,NORTH  --> plp is not an int
    '''
    def __init__(self, *args):
        if args:
            self.message = "SKIPPING: Invalid int '{}' supplied. Please supply a number with the PLACE command.".format(args[0])
    
    def __str__(self):
        if self.message:
            return '{}'.format(self.message)

