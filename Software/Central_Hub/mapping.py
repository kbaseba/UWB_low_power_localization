# Imports

# Class comment
class Mapping:
    def __init__(self, hub):
        self.collisions = []
        self.hub = hub

    def update(self):
        for data in self.hub.robotData:
            if data["button_sensor_state"]:
                self.hub.collisions.append((self.hub.robots[data["id"]].estimate_history[-1][0,0],self.hub.robots[data["id"]].estimate_history[-1][1,0]))