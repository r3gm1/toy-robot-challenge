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

    @property
    def x(self):
        '''
            using the @property --> so that we can change values of x and not have have inconsistencies
        '''
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = int(new_x) # since we are parsing from input, ensure its an int
        # TODO: probs add in error validation incase test case is 'alpha' as a coordinate

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = int(new_y)
        #TODO: add in error validation for test cases --> int wil throw an error on int('pop')
    
