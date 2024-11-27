# Imports

# This class initializes the robot's path by setting its orientation to a default value.
class PathInitialization:
    def __init__(self):
        pass

    def update(self, robot):
        # Default orientation is stationary (0, 0)
        robot.orientation = (0, 0)
