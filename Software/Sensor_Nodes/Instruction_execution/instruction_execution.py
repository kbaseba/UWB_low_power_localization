# Imports

# This class updates the robot's orientation based on the instructions received from the central hub.
class InstructionExecution:
    def __init__(self):
        pass

    def update(self, robot):
        # Update the robot's orientation from the parsed instruction
        robot.orientation = (self.received_instruction[0])
