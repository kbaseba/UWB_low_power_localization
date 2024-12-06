# Imports
from .move_robot import MoveRobot
from .transmit_data import TransmitData

# This class encapsulate instructions execution.
class InstructionExecution:
    def __init__(self, motor = MoveRobot(), transmitter_caller = TransmitData()):
        self.motor = motor
        self.transmitter_caller = transmitter_caller

    def update(self, robot):
        self.motor.update(robot = robot)
        self.transmitter_caller.update(robot = robot)
