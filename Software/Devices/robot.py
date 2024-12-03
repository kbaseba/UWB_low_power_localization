# Imports

# Class comment
class Robot:
    def __init__(self, id = 0, position = (0, 0), orientation = (0, 0), power_level = 100, role = "non-leader", data_receiver = None, executor = None,
                  sensors = None, power_harvester = None, data_transmitter = None, uwb_transmitter = None):
        self.id = id
        self.position = position
        self.orientation = orientation
        self.power_level = power_level
        self.role = role
        self.data_receiver = data_receiver
        self.executor = executor
        self.sensors = sensors
        self.power_harvester = power_harvester
        self.data_transmitter = data_transmitter
        self.uwb_transmitter = uwb_transmitter

    def update(self):
        self.executor.update()
        self.sensors.update()
        self.power_harvester.update()
        self.data_transmitter.update()
        self.uwb_transmitter.update()
        self.data_receiver.update()
