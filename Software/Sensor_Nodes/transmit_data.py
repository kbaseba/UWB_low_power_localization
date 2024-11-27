# Imports

# This class simulates the transmission of robot data to the central hub, consuming power.
class TransmitData:
    def __init__(self, energy_consum):
        self.energy_consum = energy_consum

    def update(self, robot):
        # Reduce power level for data transmission
        robot.power_level -= self.energy_consum

        # Prepare data for transmission
        data = {
            "id": robot.id,
            "position": robot.position,
            "power_level": robot.power_level,
            "light_intensity": robot.sensors.light_intensity,
            "collision_indicator": robot.collision_indicator,
        }
        self.transmitted_data = data
