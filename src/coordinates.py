from src.errors import InvalidIntError 

'''
    This class will be the one that deals with the coordinates and the position of the Toy Robot on the table.
    I will place more info as I create the functions required. 
'''
class Coordinate(object):
    def __init__(self, x=0, y=0): #initalise to be 0 if not specified
        self.x = x
        self.y = y

    def __add__(self, other):
        x = int(self.x) + int(other.x)
        y = int(self.y) + int(other.y)
        return self.__class__(x, y)

    def __eq__(self, other):
        '''
            overriding the == operator so I can use it efficiently in the pytests
        '''
        if isinstance(other, Coordinate):
            return (self.x == other.x) and (self.y == other.y)

        return False
    @property
    def x(self):
        '''
            using the @property --> so that we can change values of x and not have have inconsistencies
        '''
        return self._x

    @x.setter
    def x(self, new_x):
        try:
            self._x = int(new_x) # since we are parsing from input, ensure its an int
        except:
            raise InvalidIntError(new_x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        try:
            self._y = int(new_y)
        except:
            raise InvalidIntError(new_y)
    
