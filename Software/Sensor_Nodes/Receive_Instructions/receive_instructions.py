# Imports
import math
# This class parses received instructions to determine the robot's orientation and role.
class ReceiveInstructions:
    def __init__(self):
        pass

    def parse_instruction(self, instruction):
        # Convert the instruction's angle into an orientation vector and extract role
        orientation = (math.cos(instruction[0]), math.sin(instruction[0]))
        role = instruction[1]
        return (orientation, role)

    def update(self, robot, instruction):
        # Update the robot's received instruction
        robot.received_instuction = self.parse_instruction(instruction)
