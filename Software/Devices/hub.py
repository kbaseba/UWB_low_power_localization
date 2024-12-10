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

        self.collisions = []

        #Dictionary to store robot data by robot id
        self.robotData = [None for _ in range(len(self.robots))]

        #Dictionary for UWB localizations, keyed by robot id
        self.localizations = [[] for _ in range(len(self.robots))]

        #List of current localizations
        self.curr_localizations = []

    def receiveData(self):
        #Checking all robots for data transmission
        for robot in self.robots:
            #Is the robot is in the transmission state
            if robot.data_transmitter.state:
                #Store the data in the hub's data dictionary
                self.robotData[robot.id] = robot.data_transmitter.data


    def UWBLocalization(self):
        # Measuring location from each anchor
        measurements = []
        full_measurements = []
        avg_positions = []
        leaders = []
        self.curr_localizations = []

        for anchor in self.anchors:
            leaders = anchor.update(self.robots)
            measurement = [robot.position for robot in leaders]
            full_measurements.append(measurement)

        # Calculate average positions for each robot
        num_robots = len(full_measurements[0]) if full_measurements else 0
        for i in range(num_robots):
            measurements_for_robot = [anchor[i] for anchor in full_measurements]
            avg_x = sum(pos[0] for pos in measurements_for_robot) / len(measurements_for_robot)
            avg_y = sum(pos[1] for pos in measurements_for_robot) / len(measurements_for_robot)
            avg_positions.append((avg_x, avg_y))

        # Determine the average of the measurements to be the localization
        for i, robot in enumerate(leaders):
            robot.just_localized = True

            # Initialize the robot's localization list if not already initialized
            if robot.id not in self.localizations:
                self.localizations[robot.id] = []

            self.localizations[robot.id].append(avg_positions[i])
            self.curr_localizations.append(avg_positions[i])



    def update(self):
        #Update the three anchors, localizing leader robot
        self.UWBLocalization()