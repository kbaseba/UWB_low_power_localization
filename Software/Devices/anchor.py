# Imports

# Class comment
class Anchor:
    def __init__(self, position):
        self.position = position
        pass

    def update(self, robots):
        #Checking all the robots to see if they're transmitting UWB blinks
        for robot in robots:
            #If the uwb_transmitter signal is True, update position
            if robot.uwb_transmitter.state:
                return robot.id, robot.position
        