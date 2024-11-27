# Imports

# This class harvests power for the robot based on light intensity and updates its power level.
class PowerHarvest:
    def __init__(self, efficacy):
        self.efficacy = efficacy

    def update(self, robot):
        # Increase power level based on light intensity and harvesting efficiency
        robot.power_level += robot.sensors.light_intensity * self.efficacy
        robot.power_level = min(robot.power_level, 100)  # Cap power at 100
