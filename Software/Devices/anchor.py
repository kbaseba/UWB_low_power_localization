# Imports

# Class comment
class Anchor:
    def __init__(self, position, id):
        self.position = position
        self.id = id

    def update(self, robots):
        #Checking all the robots to see if they're transmitting UWB blinks
        leaders = []
        for robot in robots:
            #If the uwb_transmitter signal is True, update position
            if robot.uwb_transmitter.state:
                leaders.append(robot)
                
        return leaders
        