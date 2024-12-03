# Imports

class PathInitialization:
    def __init__(self):
        pass

    def update(self, robot):
        robot.orientation = robot.data_receiver.data[0]
