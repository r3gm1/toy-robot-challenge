#!/usr/bin/env python3
from src.run import Run
import sys

'''
    This file will be called upon running the Robot Challenge task
    The required files like creating the table, intercepting the commands will all automatically be run.
'''


def toy_robot():
    program = Run()

    for command in sys.stdin:
        program.run(command)


if __name__ == "__main__":
    toy_robot()
