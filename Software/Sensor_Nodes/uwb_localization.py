# Imports

# This class simulates UWB localization, where leader robots send signals to anchors.
class UWBLocalization:
    def __init__(self, energy_consum):
        self.energy_consum = energy_consum
        self.signal = False

    def update(self, robot):
        # Reduce power level for sending UWB signals
        robot.power_level -= self.energy_consum

        # Activate signal only if the robot is a leader
        if robot.role == "leader":
            self.signal = True
        else:
            self.signal = False
