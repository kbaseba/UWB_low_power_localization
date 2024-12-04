# Imports

# This class initializes the robot's path based on received data.
class PathInitialization:
    def __init__(self):
        pass

    def update(self, robot):
        # Assign the path from the parsed instruction
        robot.orientation = robot.data_receiver.data[0]
        # Reactivate the motor
        robot.executor.motor.state = True
