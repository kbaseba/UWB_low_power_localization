# Imports

""" 
The hub will receive data transmission from robots,
UWBLocalize the leader robot,
determine the next leader robot based on robot power levels,
call path planning algorithm with state estimated robot positions,
and distribute robot instructions based on path planning.
"""
class Hub:
    def __init__(self, id, position, anchors=[], robots=[]):
        self.id = id
        self.position = position
        self.anchors = anchors
        self.robots = robots

        #Dictionary to store robot data by robot id
        self.robotData = [None for _ in range(len(self.robots))]

        #Dictionary for UWB localizations, keyed by robot id
        self.localizations = [[] for _ in range(len(self.robots))]

    def receiveData(self):
        #Checking all robots for data transmission
        for robot in self.robots:
            #Is the robot is in the transmission state
            if robot.data_transmitter.state:
                #Store the data in the hub's data dictionary
                self.robotData[robot.id] = robot.data_transmitter


    def UWBLocalization(self):
        #measuring location from each anchor
        measurements = []
        for anchor in self.anchors:
            id, measuredPosition = anchor.update(self.robots)
            measurements.append(measuredPosition)
        xpos,ypos = 0,0
        for position in measurements:
            xpos += position[0]
            ypos += position[1]
        #Determining the average of the measurements to be the localization
        avgMeasuredDist = (xpos/len(self.anchors), ypos/len(self.anchors))
        self.localizations[id] = avgMeasuredDist
        pass

    def update(self):
        #Receive incoming data from robots

        #Update the three anchors, localizing leader robot
        self.UWBLocalization()