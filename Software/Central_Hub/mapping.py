# Imports

# Class comment
class Mapping:
    def __init__(self, hub):
        self.collisions = []
        self.hub = hub

    def uwb_update(self):
        for robot in self.hub.robots:
            if not robot.executor.motor.state:
                if robot.power_level > robot.power_threshold[1]:
                    robot.role = 'leader'
                    robot.just_localized = True
                    self.hub.collisions.append(robot.position)
    
    def low_power_update(self):
        for robot in self.hub.robots:
            if not robot.executor.motor.state and robot.power_level < robot.power_threshold[1]:
                self.hub.collisions.append((self.hub.robots[robot.id].estimate_history[-1][0,0],self.hub.robots[robot.id].estimate_history[-1][1,0]))
                    