# Imports

# This class simulates UWB localization, where leader robots send signals to anchors.
class UWBLocalization:
    def __init__(self, power_consum):
        """
        Initializes the UWB localization system.

        Args:
            power_consum (float): Power consumed for UWB signal transmission.
        """
        self.power_consum = power_consum
        self.state = False  # Indicates if UWB signal is active

    def update(self, robot):
        """
        Updates the UWB localization state based on the robot's role.

        Args:
            robot (object): The robot object being updated.
        """
        if robot.role == "leader" and robot.power_level > robot.power_threshold[0] and (robot.power_level - self.power_consum) >= 0:
            # Leader robots send UWB signals and consume power
            robot.power_level -= self.power_consum
            robot.role = "non-leader"
            self.state = True
        else:
            # Non-leader robots do not send signals
            self.state = False
