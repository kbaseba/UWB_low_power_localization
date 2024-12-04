# Imports

# This class harvests power for the robot based on light intensity and updates its power level.
class PowerHarvest:
    def __init__(self, efficacy):
        """
        Initializes the power harvesting system.

        Args:
            efficacy (float): The efficiency of power harvesting according to the solar cell.
        """
        self.efficacy = efficacy

    def update(self, robot):
        """
        Harvests power based on light intensity and updates the robot's power level.

        Args:
            robot (object): The robot object being updated.
        """
        # Increase power level proportional to light intensity and harvesting efficiency
        robot.power_level += robot.sensors.light_intensity * self.efficacy
        # Cap the maximum power level to 100
        robot.power_level = min(robot.power_level, 100)
        
