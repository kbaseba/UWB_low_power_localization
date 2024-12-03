# Imports
import math
import role_update
import path_initialization
# This class parses received instructions to determine the robot's orientation and role.
class ReceiveInstructions:
    def __init__(self, power_consum = 0.01):
        self.power_consum = power_consum
        self.data = None
        self.state = False
        self.role_update = role_update.RoleUpdate()
        self.path_initialization = path_initialization.PathInitialization()

    def update(self, robot, instruction = None):
        if self.state:
            # Reduce power level for data parsing
            robot.power_level -= self.power_consum
            # Convert the instruction's angle into an orientation vector and extract role
            orientation = (math.cos(instruction[0]), math.sin(instruction[0]))
            role = instruction[1]
            self.data = (orientation, role)
            self.role_update.update(robot)
            if robot.excutor.motor.state:
                self.path_initialization.update(robot)
            self.state = False

