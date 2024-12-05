# Imports

# Class comment
class Robot:
    def __init__(self, id = 0, position = (0, 0), orientation = (0, 0), power_level = 100, motor = None, sensors = None, collision_indicator = None,
                  power_harvest = None, role = "non-leader", transmitted_data = None, uwb_localization = None):
        self.id = id
        self.position = position
        self.orientation = orientation
        self.power_level = power_level
        self.motor = motor
        self.sensors = sensors
        self.collision_indicator = collision_indicator
        self.power_harvest = power_harvest
        self.role = role
        self.data_transmitter = transmitted_data
        self.uwb_transmitter = uwb_localization

    def update(self):
        """self.motor.update()
        self.sensors.update()
        self.collision_indicator.update()
        self.power_harvest.update()
        self.data_transmitter.update()
        self.uwb_transmitter.update()"""