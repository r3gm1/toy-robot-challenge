from src.input_commands import Place, Move, Left, Right, Report
from src.errors import CommandNotFoundError


class ParseInput(object):
    '''
        Will be the class used to parse the input given by the user into the actual runable code interpretted by the system.
    '''
    valid_commands = [Place, Move, Left, Right, Report]

    def parse(self, cmd):
        cmd = cmd.split(" ")
        # should now have an array that is ["command" "x,x,x"] or ["move"] e.g. 
        cmd_value = cmd[0].strip() #this is the actual cmd like: place, move, left, right, report
        args = cmd[1].lower().strip().split(',') if len(cmd) > 1 else "" # this is the 1,1,NORTH value

        for command in self.valid_commands:
            if cmd_value.lower() == command.value:
                comm = command(args)
                return comm
        
        raise CommandNotFoundError(cmd[0].strip())
