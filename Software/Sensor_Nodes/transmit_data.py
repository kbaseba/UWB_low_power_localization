# Imports

# This class simulates the transmission of robot data to the central hub
class TransmitData:
    def __init__(self, power_consum, duty_cycle):
        """
        Initializes the data transmission system.

        Args:
            power_consum (float): Power consumed per transmission cycle.
            duty_cycle (int): Number of update cycles between transmissions.
        """
        self.power_consum = power_consum
        self.duty_cycle = duty_cycle
        self.iter = 0  # Iteration counter for duty cycle
        self.state = False  # Indicates if data is being transmitted
        self.data = None  # Data to be transmitted

    def update(self, robot):
        """
        Handles data transmission and power consumption.

        Args:
            robot (object): The robot object being updated.
            power_threshold (float): Threshold for low power mode.
        """
        self.iter += 1
        # Check if the data has been sent due to collision
        if self.state: #If data is already transmitted, skip further action
            return
        else:
            # Skip transmission if not in duty cycle
            if self.iter % self.duty_cycle != 0:
                return
            # Check if the robot is in low power mode
            if robot.mode == "low power":
                return
            # Check if the robot has enough power for transmission
            self.state = True
            # Reduce power level for data transmission
            robot.power_level -= self.power_consum
            # Prepare data for transmission
            self.data = {
                "id": robot.id,
                "mode": robot.mode,
                "power_level": robot.power_level,
                "light_intensity": robot.sensors.light_intensity,
                "button_sensor_state": robot.sensors.button_sensor
            }