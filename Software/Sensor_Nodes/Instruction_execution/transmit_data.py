# Imports


# This class handles data transmission for the robot after movement.
class TransmitData:
    def __init__(self):
        pass

    def update(self, robot):
        """
        Transmit data if collision is found.

        Args:
            robot (object): The robot object being updated.
        """
        # Check if collision is detected
        if not robot.senser_nodes.button_sensor:
            return
        else:
            robot.data_transmitter.state = True
            # Reduce power level for data transmission
            robot.power_level -= robot.data_transmitter.power_consum
            # Prepare data for transmission
            data = {
                "id": robot.id,
                "mode": robot.mode,
                "power_level": robot.power_level,
                "light_intensity": robot.sensors.light_intensity,
                "button_sensor_state": robot.senser_nodes.button_sensor
            }
            robot.data_transmitter.data = data
