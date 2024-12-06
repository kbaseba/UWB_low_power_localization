# Imports
from .move_robot import MoveRobot
from .transmit_data import TransmitData

# This class encapsulate instructions execution.
class InstructionExecution:
    def __init__(self, system_simulator, motor = MoveRobot(), transmitter_caller = TransmitData()):
        self.motor = motor
        self.transmitter_caller = transmitter_caller
        self.system_simulator = system_simulator

    def update(self, robot, map, robots):
        self.motor.update(robot, map, robots, self.system_simulator)
        self.transmitter_caller.update(robot = robot)
