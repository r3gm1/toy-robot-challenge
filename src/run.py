from src.toy_robot import ToyRobot
from src.table import Table
from src.parse_input import ParseInput
from src.errors import * # import all the error classes

class Run(object):
    def __init__(self):
        self.parse_input = ParseInput()
        self.reset()

    def reset(self):
        self.table = Table()
        self.robot = ToyRobot(self.table)

    def run(self, line):
        try:
            command  = self.parse_input.parse(line.lower())
        except InvalidPlaceCommandError as e:
            print(e)
            return
        except CommandNotFoundError as e:
            print(e)
            return
        except InvalidIntError as e:
            print(e)
            return


        if not command:

            print('')
            return

        try:
            command.execute(self.robot)
        except OffTableError as e:
            # show the error to the user 
            print(e)
            return 
        except NoCoordinateError as e:
            print(e)
            return 
        except InvalidDirectionError as e:
            print(e)
            return 

        return
