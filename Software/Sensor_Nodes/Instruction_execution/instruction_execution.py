# Imports
import move_robot
import transmit_data

# This class encapsulate instructions execution.
class InstructionExecution:
    def __init__(self, motor = move_robot.MoveRobot(), transmitter_caller = transmit_data.TransmitData()):
        self.motor = motor
        self.transmitter_caller = transmitter_caller

    def update(self, robot):
        self.motor.update(robot = robot)
        self.transmitter_caller.update(robot = robot)
