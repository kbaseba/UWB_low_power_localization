import random

class RandomWalk:
    def __init__(self, hub):
        self.hub = hub

    def update(self, map):
        for robot in self.hub.robots:
            # Check if the robot has hit an obstacle (motor state is False)
            if not robot.executor.motor.state:
                # Flip orientation by 180 degrees
                # flipped_orientation = (robot.orientation + 180) % 360

                # Define the valid range as ±90° from the flipped orientation
                lower_bound = (robot.orientation - 90) % 360
                upper_bound = (robot.orientation + 90) % 360

                # Handle angle wrapping
                if lower_bound < upper_bound:
                    # Case where angles do not cross 0°
                    new_orientation = random.uniform(lower_bound, upper_bound)
                else:
                    # Case where angles cross 0°, split into two ranges
                    angle_part1 = random.uniform(lower_bound, 360)
                    angle_part2 = random.uniform(0, upper_bound)
                    new_orientation = random.choice([angle_part1, angle_part2])

                # Update the robot's orientation to a valid direction
                robot.orientation = new_orientation

                # Reactivate the motor
                robot.executor.motor.state = True
