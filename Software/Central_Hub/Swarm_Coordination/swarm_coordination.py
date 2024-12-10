from .potential_field_computation import PotentialFieldComputation

class SwarmCoordination:
    def __init__(self, hub):
        self.hub = hub

    def update(self, map):
        for robot in self.hub.robots:
            if not robot.excutor.motor.state:
                PotentialFieldComputation(map=map, hub=self.hub, robot=robot).update()
                robot.executor.motor.state = True
