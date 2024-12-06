# Imports
from .potential_field_computation import PotentialFieldComputation
# Class comment
class SwarmCoordination:
    def _init_(self,hub):
        self.hub=hub

    def update(self,map,hub):
        for data in self.hub.robotData:
            if data["button_sensor_state"]:
                print(self.hub.robots[data["id"]])
                PotentialFieldComputation(map=map,hub=hub, robot=self.hub.robots[data["id"]]).update()
                self.hub.robots[data["id"]].excutor.motor.state = True