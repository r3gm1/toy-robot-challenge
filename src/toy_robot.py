from src.errors import OffTableError, NoCoordinateError

class ToyRobot(object):
    '''
        This class will be responsible for the actual Toy Robot itself.
    '''
    def __init__(self, table):
        self._table = table
        self._direction = None
        self._coordinate = None
    

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        # check if the new coordinates are valid by calling the function created
        valid = self._table.table_boundaries.valid_coordinate(coordinate)
        if not valid:
            #print('Robot will fall of table')
            raise OffTableError()
        
        self._coordinate = coordinate


    @property
    def table(self):
        return self._table

    def place_robot(self, coordinate, direction):
        '''
            Will be used to 'place' the toy robot on the table 
            provided coordinates are within constraints.
        '''
        if coordinate and direction:
            # ensure they are not 'None'
            self.direction = direction
            self.coordinate = coordinate
    

    def turn_robot(self, direction):
        '''
            This function will be used to change the direction of the robot
        '''
        if not self._direction:
            # ensure the direction is set before actually turning
            raise NoCoordinateError()
        
        new_direction = self._direction.turn(direction)
        self.direction = new_direction

    def move_robot(self):
        '''
            Used to move the toy robot to new coordinates on the table
        '''
        # check if the coordinates and direction are still None
        if not self._coordinate:
            raise NoCoordinateError()

        new_coordinates = self._coordinate + (self._direction.position )
        self.coordinate = new_coordinates



    def print_current_status(self):
        '''
            This method will be called when the 'report' command has been entered.
            It will output the current status of the robot on the table

        '''
        # check if direction and coordinates are placed
        if not (self._direction or self._coordinate):
            raise NoCoordinateError()
        status = "Output: {},{},{}".format(self._coordinate.x, self._coordinate.y, self._direction.direction.upper())

        return status


