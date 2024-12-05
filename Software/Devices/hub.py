# Imports

# Class comment
class Hub:
    def __init__(self, robots=[], anchors=[]):
        self.robots = robots
        self.anchors = anchors
    def __init__(self, robots=[], anchors=[]):
        self.robots = robots
        self.anchors = anchors
        pass

    def update(self):
        #Update the three anchors, localizing leader robot
        anchorMeasurements = []
        for anchor in self.anchors:
            anchorMeasure = anchor.update(self.robots)
            anchorMeasurements.append(anchorMeasure)
        #If no robots are assigned leader
        num_anchorsMeasurements = len(anchorMeasurements)
        if num_anchorsMeasurements==0:
            #print('No leader robots')
            pass
        else:
            xpos,ypos = 0,0
            for position in anchorMeasurements:
                xpos += position[0]
                ypos += position[1]
            avgMeasuredDist = (xpos/num_anchorsMeasurements, ypos/num_anchorsMeasurements)
            print(avgMeasuredDist)
            return avgMeasuredDist