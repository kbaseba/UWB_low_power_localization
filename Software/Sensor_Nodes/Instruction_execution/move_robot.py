# Imports

# This class moves the robot in its current orientation and updates its power level accordingly.
class MoveRobot:
    def __init__(self, power_consum = 1, velocity = 0.1):
        """
        Initializes the movement system for the robot.

        Args:
            power_consum (float): Power consumed per movement step.
            velocity (float): Movement velocity per update.
        """
        self.power_consum = power_consum
        self.velocity = velocity
        self.state = False  # Indicates whether the robot can move.

    def update(self, robot):
        """
        Updates the robot's position and power level.

        Args:
            robot (object): The robot object being updated.
            power_threshold (float): Power threshold for low power mode.
        """
        # Check if the robot is in low power mode
        if robot == "low power":
            return
        # Reduce power for movement
        robot.power_level -= self.power_consum
        # Move forward if no collision is found
        if self.state:
            if robot.senser_nodes.button_sensor:
                # Reverse movement
                robot.position = (
                    robot.position[0] - self.velocity * robot.orientation[0],
                    robot.position[1] - self.velocity * robot.orientation[1],
                )
                self.state = False
            else:
                # Forward movement
                robot.position = (
                    robot.position[0] + self.velocity * robot.orientation[0],
                    robot.position[1] + self.velocity * robot.orientation[1],
                )
        # Update sensor readings after movement
            robot.sensors.update()
        

