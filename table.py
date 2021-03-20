import math
from coordinates import Coordinate

'''
    This class will be the table itself.
    Since the requirements mention a 5 X 5 table, then it will automatically generate a 5 X 5.
    EXTENSIBILITY: We may want to make it a bit extensible by allowing such a table to be made based on parameters.
'''
class Table(object):
    def __init__(self):
        origin = Coordinate(0,0) # south west most corner as specified in the SPEC
        max_top_right = Coordinate(4,4) #The highest and most-right point north-east most corner
        # therefore the table we can create using these constraints
        self.table = TableCoordinates(origin, max_top_right)

    
class TableCoordinates(object):
    '''
        This class will be responsible for holding the table coordinates  
        We know that currently the table will be 5 X 5.
        So for now code it such that a 5X5 table is auto created, however maybe have extensibility such that 
        any dimension can be passed as arguments and then create the table.

        The parameters: origin and max_top_right --> convey the size of the table that are the constraint
        and Robot should not have coorinates that exceed these points. 
    '''
    def __init__(self, origin, max_top_right):
        # origin is mosth south west
        # max_top_right is most north east
        # use these to create the max most constraints of the table.
        self._max_top = max(origin.y, max_top_right.y)
        self._max_bottom = min(origin.y, max_top_right.y)

        self._max_right = max(origin.x, max_top_right.x)
        self._max_left = min(origin.x, max_top_right.x)
         
    @property 
    def max_top(self):
        return self._max_top

    @property
    def max_bottom(self):
        return self._max_bottom
    
    @property
    def max_right(self):
        return self._max_right

    @property
    def max_left(self):
        return self._max_left_

     
