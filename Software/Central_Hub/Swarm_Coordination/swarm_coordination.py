from .potential_field_computation import PotentialFieldComputation

class SwarmCoordination:
    def __init__(self, hub):
        self.hub = hub

    def update(self, map):
        for data in self.hub.robotData:
            if data["button_sensor_state"]:
                PotentialFieldComputation(map=map, hub=self.hub, robot=self.hub.robots[data["id"]]).update()
                self.hub.robots[data["id"]].executor.motor.state = True
                data["button_sensor_state"] = False
