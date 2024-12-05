# Imports

# Class comment
class Hub:
    def __init__(self, robots=[], anchors=[]):
        self.robots = robots
        self.anchors = anchors
        pass

    def update(self):
        #Assign leader to robot with highest power
        leaderID= 
        for robot in self.robots:


        #Update the three anchors, localizing leader robot
        anchorMeasurements = []
        for anchor in self.anchors:
            anchorMeasure = anchor.update(self.robots)
            anchorMeasurements.append(anchorMeasure)
        xpos,ypos = 0,0
        for position in anchorMeasurements:
            xpos += position[0]
            ypos += position[1]
        avgMeasuredDist = (xpos/num_anchorsMeasurements, ypos/num_anchorsMeasurements)
        print(avgMeasuredDist)
        return avgMeasuredDist