# Imports

# This class updates the robot's role based on its received instructions.
class RoleUpdate:
    def __init__(self):
        pass

    def update(self, robot):
        # Assign the role from the parsed instruction
        robot.role = robot.data_receiver.data[1]
