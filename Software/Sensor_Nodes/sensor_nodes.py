# Imports
import numpy as np
from shapely.geometry import Point, Polygon
# This class updates the robot's sensor readings, including light intensity and collision detection.
class SensorNodes:
    def __init__(self):
        """
        Initialize the sensor nodes with default values.
        """
        self.light_intensity = None  # Light intensity at the robot's current position
        self.button_sensor = False  # State of the button sensor (collision detection)

    def update(self, robot, map):
        # Update light intensity based on the robot's position on the map
        self.light_intensity = map.light_map[robot.position[1], robot.position[0]]
        
        # Check collision with obstacles
        for obs in self.obstacles:
            if obs[0] == "rectangle":
                _, rect_x, rect_y, rect_w, rect_h = obs
                if rect_x <= robot.position[0] <= rect_x + rect_w and rect_y <= robot.position[1] <= rect_y + rect_h:
                    self.button_sensor = True
                    break

            elif obs[0] == "circle":
                _, cx, cy, r = obs
                distance = np.sqrt((robot.position[0] - cx)**2 + (robot.position[1] - cy)**2)
                if distance <= r:
                    self.button_sensor = True
                    break

            elif obs[0] == "polygon":
                _, points = obs
                polygon = Polygon(points)
                if polygon.contains(Point(robot.position[0], robot.position[1])):
                    self.button_sensor = True
                    break

        # Check collision with other robots
        for other_robot in map.robots:
            if other_robot != robot:  # Avoid self-collision check
                if abs(robot.position[0] - other_robot.position[0]) < 1 and abs(robot.position[1] - other_robot.position[1]) < 1:
                    self.button_sensor = True
                    break

        self.button_sensor = False

