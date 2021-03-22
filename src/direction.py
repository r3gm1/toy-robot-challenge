from src.coordinates import Coordinate
'''
    This class will be responsible for the direction aspect of the moving robot.
'''

class Direction(object):
    direction_values = ['north', 'east', 'south', 'west'] # use this to check if user input value is valid
    
    # below is a dict that stores the base positions for each direction
    positions = {
            'north': Coordinate(0,1),
            'east': Coordinate(1, 0),
            'south': Coordinate(0,-1),
            'west': Coordinate(-1, 0),
    }

    def __init__(self, direction):
        if direction not in self.direction_values:
            # TODO: here we should handle an error --
            print('invalid', direction)
            return

        self._direction = direction

    def __eq__(self, other):
        if isinstance(other, Direction):
            return (self.position == other.position)


    @property
    def position(self):
        '''
            return the current position
        '''
        return self.positions[self._direction]

    @property
    def direction(self):
        '''
            return the actual direction the robot is facing
        '''
        return self._direction


    def turn(self, direction):
        '''
           Method will be used to move the robot by 'x' 'direction(s)' on the table
        '''
        # first start by getting position of 'direction' in the list
        position = self.direction_values.index(self._direction)
        # now to calculate the new position, we can use mod since there are only 4 possible values for direction
        # so mathematically: if the direction is 3, and position is 1 --> (3 + 1) mod 4 = 0 and therefore would be North
        direction_position = (position + direction) % 4 # ==> 4 as there are 4 directions

        return self.__class__(self.direction_values[direction_position])




