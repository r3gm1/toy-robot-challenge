import pytest
from src.parse_input import *
from src.toy_robot import ToyRobot
from src.table import Table
from src.direction import Direction
from src.coordinates import Coordinate
from src.errors import CommandNotFoundError


class TestParseInput():
    '''
        This class will be used to test the ParseInput.
    '''
    parse_input = ParseInput()
    table = Table() #used for thorough testing
    robot = ToyRobot(table) #used for thorough testing full way through

    def test_place_parse(self):
        '''
            Testing the 'place' command. checking if it returns the expected
        '''
        cmd = self.parse_input.parse("place 1,2,east")
         
        assert cmd.value == "place"
        assert cmd.args == ["1", "2", "east"]

    def test_case_insensitive_place(self):
        '''
            Ensuring the place command is case insensitive
        '''
        cmd = self.parse_input.parse("PLaCE 1,2,EaST")

        assert cmd.value == "place"
        assert cmd.args == ["1", "2", "east"]

    def test_move_parse(self):
        '''
            Testing if the 'move' command is successfully parsed as expected
        '''

        cmd = self.parse_input.parse("move")
        assert cmd.value == "move"

    def test_thorough_move_robot(self):
        ''' 
            This test will be a thorough test, with a few different components to see if they all
            work well together 
        '''


        cmd = self.parse_input.parse("place 1,2,east")
        cmd.execute(self.robot)

        ## check the parse
        assert cmd.value == "place"
        assert cmd.args == ["1", "2", "east"]

        ## check the robot
        assert self.robot.coordinate == Coordinate(1,2)
        assert self.robot.direction == Direction("east")
        

        
    def test_cmd_not_found(self):
        '''
            This function aims to test an invalid command 
        '''
        with pytest.raises(CommandNotFoundError):
            cmd = self.parse_input.parse("autocomplete_code")








