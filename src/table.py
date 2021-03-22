import math
from src.coordinates import Coordinate

'''
    This class will be the table itself.
    Since the requirements mention a 5 X 5 table, then it will automatically generate a 5 X 5.
    EXTENSIBILITY: We may want to make it a bit extensible by allowing such a table to be made based on parameters.
'''
class Table(object):
    def __init__(self, size_horizontal=5, size_vertical=5):
        origin = Coordinate(0,0) # south west most corner as specified in the SPEC
        #max_top_right = Coordinate(4,4) #The highest and most-right point north-east most corner
        max_top_right = Coordinate((size_horizontal - 1), (size_vertical - 1)) # dynamic table size
        # therefore the table we can create using these constraints
        self.table_boundaries = TableCoordinates(origin, max_top_right)

    
class TableCoordinates(object):
    '''
        This class will be responsible for holding the table coordinates  
        We know that currently the table will be 5 X 5.
        So for now code it such that a 5X5 table is auto created, however maybe have extensibility such that 
        any dimension can be passed as arguments and then create the table. ## UPDATE --> has been updated such that table size can change

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
    def max_left(self):
        return self._max_left

    @property
    def max_right(self):
        return self._max_right

    def value_between(self, tested, val_one, val_two):
        '''
            Used to check if param 'tested' value is between val_one and val_two [inclusive]
        '''
        return (int(tested) >= int(val_one)) and (int(tested) <= int(val_two))


    def valid_coordinate(self, coordinate):
        '''
            Check if the 'coordinate' parameter is within the constraints of the table
        '''
        valid_x_value = self.value_between(coordinate.x, self._max_left, self._max_right)
        valid_y_value = self.value_between(coordinate.y, self._max_bottom, self._max_top)

        return valid_x_value and valid_y_value
        


     
