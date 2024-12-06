# Imports
from .potential_field_computation import PotentialFieldComputation
# Class comment
class SwarmCoordination:
    def __init__(self,hub):
        self.hub=hub

    def update(self,map):
        for data in self.hub.robotData:
            if data["button_sensor_state"]:
                print(self.hub.robots[data["id"]].orientation)
                PotentialFieldComputation(map=map,hub=self.hub, robot=self.hub.robots[data["id"]]).update()
                print(self.hub.robots[data["id"]].orientation)
                self.hub.robots[data["id"]].executor.motor.state = True
                data["button_sensor_state"] = False