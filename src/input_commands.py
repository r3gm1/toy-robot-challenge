from direction import Direction
from coordinates import Coordinate

'''
    So all the classes: 
    - Move, Place, Report, Turn will have a function called 'execute' 
    - this is so when we parse the user's input [i.e. command] --> we can call the .execute on all classes
    - all commands are in 'lowercase' so that its case insensitive --> this is intentionally done
'''

class Input():
    '''
        This class will aid in parsing the input from the user 
        It will be the basic class
    '''
    _args = [] # list of arguments supplied 
    value = ""
    
    def __init__(self, args=None):
        self.args = args 

    @property
    def args(self):
        return self._args


    @args.setter
    # need this so that we can use fset for the place command
    def args(self, argument_values):
        self._args = argument_values

class Place(Input):
    '''
        This function will call the 'PLACE' command.
        it checks the arguments of input and then executes allows invokation of method.
    '''
    value = "place"

    @Input.args.setter
    def args(self, argument_values):
        Input.args.fset(self, argument_values)
        (x,y,direction) = argument_values

        self._coordinate = Coordinate(x, y)
        self._direction = Direction(direction)
    
    def execute(self, robot):
        '''
            actually perform the 'place' command
        '''
        (x, y, direction) = self._args
        if not self._coordinate:
            self._coordinate = Coordinate(x,y)
        if not self._direction:
            self._direction = Direction(direction)

        robot.place_robot(self._coordinate, self._direction) #call the robot function --> 

class Report(Input):
    '''
        This class will be used to output the current status of the toy robot on the table
    '''
    value = "report"
    def execute(self, robot):
        print("OUTPUT: {}".format(robot.print_current_status()))
        return


class Move(Input):
    '''
        move the robot accordingly 
    '''
    value = "move"

    def execute(self, robot):
        robot.move_robot()
        return
    


class Left(Input):
    '''
       This class will call the turn_robot function which will basically 
       change the position towards the left. i.e. by -1.
       so if we have a list ['north', 'east', 'south', 'west']
       and robot is currently at east, if we turn left: index of east is 1
       and 1-1 = 0 and therefore the robot is now facing north.
    '''
    value = "left"
    def execute(self, robot):
        robot.turn_robot(-1)
        return


class Right(Input):
    '''
       This class will call the turn_robot function which will basically 
       change the position towards the right . i.e. by 1.
       so if we have a list ['north', 'east', 'south', 'west']
       and robot is currently at east, if we turn right: index of east is 1
       and 1 + 1 = 2 and therefore the robot is now facing south.
    '''
    value = "right"
    def execute(self, robot):
        robot.turn_robot(1)
        return
