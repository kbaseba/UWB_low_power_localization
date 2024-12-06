# Imports
from numpy import random

# Class comment
class Anchor:
    def __init__(self, position, id):
        self.position = position
        self.id = id
        pass

    def update(self, robots):
        #Checking all the robots to see if they're transmitting UWB blinks
        for robot in robots:
            #If the uwb_transmitter signal is True, update position
            if robot.uwb_transmitter.state:
                measuredPosition = random.normal(robot.position, 0.01)
                return robot.id, measuredPosition
        