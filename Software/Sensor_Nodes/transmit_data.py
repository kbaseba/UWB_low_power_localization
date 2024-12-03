# Imports

# This class simulates the transmission of robot data to the central hub, consuming power.
class TransmitData:
    def __init__(self, power_consum, duty_cycle):
        self.power_consum = power_consum
        self.duty_cycle = duty_cycle
        self.iter = 0
        self.state = False
        self.data = None

    def update(self, robot, power_threshold):
        # Check if the data has sent the data due to collision
        if self.state == True:
            return
        else:
            # Check if the data transmitter is not in duty
            if self.iter % self.duty_cycle != 0:
                return
            else:
                # Check if the robot is in low power mode
                if robot.power_level < power_threshold:
                    return
                else:
                    self.state = True
                    # Reduce power level for data transmission
                    robot.power_level -= self.power_consum
                    # Prepare data for transmission
                    data = {
                        "id": robot.id,
                        "power_level": robot.power_level,
                        "light_intensity": robot.sensors.light_intensity,
                        "button_sensor_state": robot.senser_nodes.button_sensor
                    }
                    self.data = data