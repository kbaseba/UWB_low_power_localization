# Imports

# This class simulates UWB localization, where leader robots send signals to anchors.
class UWBLocalization:
    def __init__(self, power_consum):
        self.power_consum = power_consum
        self.state = False

    def update(self, robot):
        # Activate signal only if the robot is a leader
        if robot.role == "leader":
            # Reduce power level for sending UWB signals
            robot.power_level -= self.power_consum
            self.state = True
        else:
            self.state = False
