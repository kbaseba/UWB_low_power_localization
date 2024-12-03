# Imports

# This class moves the robot in its current orientation and updates its power level accordingly.
class MoveRobot:
    def __init__(self, power_consum = 1, velocity = 0.1):
        self.power_consum = power_consum
        self.velocity = velocity
        self.state = True

    def update(self, robot, power_threshold = 10):
        # Only move if the robot has enough power
        if robot.power_level < power_threshold:
            # Reduce power for movement
            robot.power_level -= self.power_consum
            # Move forward if no collision is found
            if self.state == True:
                if robot.senser_nodes.button_sensor:
                    robot.position = (
                        robot.position[0] - self.velocity * robot.orientation[0],
                        robot.position[1] - self.velocity * robot.orientation[1],
                    )
                    self.state = False
                else:
                    robot.position = (
                        robot.position[0] + self.velocity * robot.orientation[0],
                        robot.position[1] + self.velocity * robot.orientation[1],
                    )

