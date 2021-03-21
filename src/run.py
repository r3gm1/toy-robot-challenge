from toy_robot import ToyRobot
from table import Table
from parse_input import ParseInput

class Run(object):
    def __init__(self):
        self.parse_input = ParseInput()
        self.reset()

    def reset(self):
        self.table = Table()
        self.robot = ToyRobot(self.table)

    def run(self, line):
        command  = self.parse_input.parse(line)
        #TODO: remove args from above line
        if not command:
            print('')
            return
        command.execute(self.robot)
        return
