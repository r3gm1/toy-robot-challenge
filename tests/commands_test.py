import pytest

from src.table import Table
from src.input_commands import *
from src.toy_robot import ToyRobot
from src.direction import Direction
from src.coordinates import Coordinate

class TestInputCommands():
    '''
        This class will be used to test the input commands.
        Input commands can be "PLACE X,Y,F", "MOVE", "LEFT", "RIGHT", "REPORT"
    '''
    table = Table()
    robot = ToyRobot(table)
    
    def test_place_command(self):
        '''
            Will be used to test the place command 
        '''
        #TODO: make another test file to test parse_input to see if commands are parsed successfully
        cmd = Place(["1", "2", "east"])
        cmd.execute(self.robot)
        assert self.robot.coordinate == Coordinate(1,2)
        assert self.robot.direction == Direction("east")

    #TODO: In the program throw some exceptions --> so that we can test if the correct exceptions are thrown

    def test_move_command(self):
        '''
            This function will test the move command to see if the coordinate updates as expected
        '''
        cmd = Place(["1", "2", "east"])
        cmd.execute(self.robot)

        # now issue the move command
        cmd = Move()
        cmd.execute(self.robot)

        # at this point the coordinate should be 2,2
        assert self.robot.coordinate == Coordinate(2,2)
        assert self.robot.direction == Direction("east")





    
