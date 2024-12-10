# Imports
import numpy as np
from shapely.geometry import Point, Polygon
import math

# This class updates the robot's sensor readings, including light intensity and collision detection.
class SensorNodes:
    def __init__(self):
        self.light_intensity = None  # Light intensity at the robot's current position
        self.button_sensor = False  # State of the button sensor (collision detection)

    def update(self, robot, map, robots):
        """
        Updates sensor readings for the robot, including light intensity and collision detection.

        Args:
            robot (object): The robot object being updated.
            map (object): The map object containing light and obstacle data.
        """
        # Update light intensity based on the robot's position on the map
        self.light_intensity = map.light_map[math.floor(robot.position[0])-1, math.floor(robot.position[1])-1]

        # Check for collisions with boundaries
        self.button_sensor = False

        if robot.position[0]+robot.velocity*math.cos((robot.orientation/360)*2*math.pi) < 0 or robot.position[0]+robot.velocity*math.cos((robot.orientation/360)*2*math.pi) >= map.width-1 or robot.position[1]+robot.velocity*math.sin((robot.orientation/360)*2*math.pi) < 0 or robot.position[1]+robot.velocity*math.sin((robot.orientation/360)*2*math.pi) >= map.height-1:
            self.button_sensor = True
            

        # Check for collisions with obstacles
        for obs in map.obstacles:
            if obs[0] == "rectangle":
                # Check if the robot collides with the rectangle
                _, rect_x, rect_y, rect_w, rect_h = obs
                if rect_x <= robot.position[0]+robot.velocity*math.cos((robot.orientation/360)*2*math.pi) <= rect_x + rect_w and rect_y <= robot.position[1]+ robot.velocity*math.sin((robot.orientation/360)*2*math.pi) <= rect_y + rect_h:
                    self.button_sensor = True
                    break

            elif obs[0] == "circle":
                # Check if the robot collides with the circle
                _, cx, cy, r = obs
                distance = np.sqrt((robot.position[0]+robot.velocity*math.cos((robot.orientation/360)*2*math.pi) - cx)**2 + (robot.position[1]+ robot.velocity*math.sin((robot.orientation/360)*2*math.pi) - cy)**2)
                if distance <= r:
                    self.button_sensor = True
                    break

            elif obs[0] == "polygon":
                # Check if the robot collides with the polygon
                _, points = obs
                polygon = Polygon(points)
                if polygon.contains(Point(robot.position[0]+robot.velocity*math.cos((robot.orientation/360)*2*math.pi), robot.position[1]+ robot.velocity*math.sin((robot.orientation/360)*2*math.pi))):
                    self.button_sensor = True
                    break

        # Check for collisions with other robots within the robot's field of view (within -90° to 90° of the robot's orientation)
        # for other_robot in robots:
        #     if other_robot.id != robot.id:  # Ignore self-collision check
        #         # Calculate the vector from the robot to the other robot
        #         distance_x = other_robot.position[0] - robot.position[0]
        #         distance_y = other_robot.position[1] - robot.position[1]

        #         # Calculate the distance between the robots
        #         distance = math.sqrt(distance_x**2 + distance_y**2)

        #         if distance < 5:  # Adjust collision distance threshold as needed
        #             # Normalize the vector (distance_x, distance_y) to get the direction
        #             # print(f"distance: {distance}")

        #             direction_vector = (distance_x / distance, distance_y / distance)

        #             # Get the robot's orientation as a unit vector
        #             orientation_vector = (
        #                 math.cos(math.atan2( math.sin((robot.orientation/360)*2*math.pi), math.cos((robot.orientation/360)*2*math.pi))),
        #                 math.sin(math.atan2( math.sin((robot.orientation/360)*2*math.pi), math.cos((robot.orientation/360)*2*math.pi))),
        #             )

        #             # Calculate the dot product to find the angle between vectors
        #             dot_product = (
        #                 direction_vector[0] * orientation_vector[0]
        #                 + direction_vector[1] * orientation_vector[1]
        #             )

        #             # Use the dot product to check if the angle is within -90° to 90°
        #             angle = math.degrees(math.acos(dot_product))
        #             if -90 <= angle <= 90:
        #                 self.button_sensor = True
        #                 return  # Exit loop after detecting collision
    