import pytest
from src.toy_robot import ToyRobot
from src.table import Table
from src.direction import Direction
from src.coordinates import Coordinate
from src.errors import OffTableError, NoCoordinateError, InvalidIntError

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
        self.robot.turn_robot(-1) # left is -1 and right it 1
        self.robot.move_robot()

        # at this point the robot should be at 3,3,NORTH
        assert self.robot.coordinate == Coordinate(3, 3)
        assert self.robot.direction == Direction("north")
    

    def test_right_turns(self):
        '''
            Place the robot on the table and test by turning all the way right
        '''
        self.robot.place_robot(Coordinate(1,1), Direction("south"))
        
        self.robot.turn_robot(1) # left is -1 and right it 1
        assert self.robot.direction == Direction("west")

        self.robot.turn_robot(1) # left is -1 and right it 1
        assert self.robot.direction == Direction("north")

        self.robot.turn_robot(1) # left is -1 and right it 1
        assert self.robot.direction == Direction("east")
        
        self.robot.turn_robot(1) # left is -1 and right it 1
        assert self.robot.direction == Direction("south")


    def test_left_turns(self):
        '''
            Place the robot and then test by turning all the way left to see if each direction
            works
        '''
        self.robot.place_robot(Coordinate(1,1), Direction("south"))
        
        self.robot.turn_robot(-1) # left is -1 and right it 1
        assert self.robot.direction == Direction("east")

        self.robot.turn_robot(-1) # left is -1 and right it 1
        assert self.robot.direction == Direction("north") #should be north

        self.robot.turn_robot(-1) # left is -1 and right it 1
        assert self.robot.direction == Direction("west") #should be west 


        self.robot.turn_robot(-1) # left is -1 and right it 1
        assert self.robot.direction == Direction("south") #should be south 


    def test_off_table_error(self):
        '''
            This function aims to test the OffTableError and checks if it gets raised
        '''
        with pytest.raises(OffTableError):
            self.robot.place_robot(Coordinate(5,5), Direction("east"))

    def test_move_no_coordinate(self):
        '''
            This function will test if a NoCoordinateError is thrown if the robot is 
            'moved' without issuing the place command
        '''
        self.robot = ToyRobot(self.table) #instantiate a new one for testing this
        with pytest.raises(NoCoordinateError):
            self.robot.move_robot()

    def test_right_no_coordiate(self):
        '''
            This function will test if a NoCoordinateError is thrown if the robot is 
            issued 'right'  without issuing the place command
        '''
        self.robot = ToyRobot(self.table) #instantiate a new one for testing this
        with pytest.raises(NoCoordinateError):
            self.robot.turn_robot(1)

    def test_left_no_coordiate(self):
        '''
            This function will test if a NoCoordinateError is thrown if the robot is 
            issued 'left'  without issuing the place command
        '''
        self.robot = ToyRobot(self.table) #instantiate a new one for testing this
        with pytest.raises(NoCoordinateError):
            self.robot.turn_robot(-1)


    def test_invalid_int_coordinates(self):
        '''
            This function will test invalid coordinates as in ('alpha', 2) -> alpha is not int
                so should throw an error
        '''
        with pytest.raises(InvalidIntError):
            self.robot.place_robot(Coordinate('alpha', 0), Direction("east"))
            
    






