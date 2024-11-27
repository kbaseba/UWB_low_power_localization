# Imports

# This class moves the robot in its current orientation and updates its power level accordingly.
class MoveRobot:
    def __init__(self, power_consumption_factor):
        self.power_consumption_factor = power_consumption_factor

    def update(self, robot):
        # Only move if the robot has enough power and no collision is detected
        if robot.power_level < 5 and not robot.collision_indicator:
            robot.position = (
                robot.position[0] + robot.orientation[0],
                robot.position[1] + robot.orientation[1],
            )

        # Reduce power for movement
        robot.power_level -= self.power_consumption_factor
