
from src.toy_robot import *
from src.table import Table
from src.direction import Direction
from src.coordinates import Coordinate

class TestRobot():
    table = Table()
    robot = ToyRobot(table)

    def test_place(self):
        '''
            This function will be used to test if the 'place' function works in Robot's method
        '''
        self.robot.place_robot(Coordinate(0,0), Direction("east"))
        assert self.robot.coordinate == Coordinate(0,0)
        assert self.robot.direction == Direction("east")

    def test_place_move(self):
        '''
            Will be used to test the place functionality and the move functionality
        '''
        self.robot.place_robot(Coordinate(1,2), Direction("east"))
        self.robot.move_robot()
        self.robot.move_robot()
        # at this point the new coordinate should be 3,2 
        assert self.robot.coordinate == Coordinate(3, 2)
        assert self.robot.direction == Direction("east")


    def test_place_move_turn(self):
        '''
            This test will placing the robot, moving it, and turning it
        '''
        self.robot.place_robot(Coordinate(1,2), Direction("east"))
        self.robot.move_robot()
        self.robot.move_robot()
        self.robot.turn_robot(-1) # left is -1
        self.robot.move_robot()

        # at this point the robot should be at 3,3,NORTH
        assert self.robot.coordinate == Coordinate(3, 3)
        assert self.robot.direction == Direction("north")


