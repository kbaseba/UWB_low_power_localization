import numpy as np
from shapely.geometry import Point, Polygon, box

from Devices.robot import Robot

# Class comment
class NodePlacement:
    """
    Strategically positions sensor nodes, UWB anchors, and the central hub
    within each sector to ensure effective localization, communication, and data collection.
    """
    def __init__(self, total_num_sensor_nodes, node_range, obstacles):
        self.total_num_sensor_nodes = total_num_sensor_nodes  # Total number of sensor nodes
        self.node_range = node_range  # Communication range of each node
        self.obstacles = obstacles  # List of obstacles on the map
        self.robots = []  # List of Robot objects

    def is_valid_position(self, x, y):
        """
        Check if a position is valid (i.e., not inside any obstacle).
        """
        point = Point(x, y)
        for obs in self.obstacles:
            if obs[0] == "rectangle":
                _, x0, y0, w, h = obs
                rect = box(x0, y0, x0 + w, y0 + h)
                if rect.contains(point):
                    return False
            elif obs[0] == "circle":
                _, cx, cy, r = obs
                circle = Point(cx, cy).buffer(r)
                if circle.contains(point):
                    return False
            elif obs[0] == "polygon":
                _, points = obs
                poly = Polygon(points)
                if poly.contains(point):
                    return False
        return True

    def update(self, sectors):
        """
        Place nodes randomly within the bounds of each sector, avoiding obstacles,
        and instantiate them as Robot objects.
        """
        self.robots = []  # Reset the list of robots

        # Calculate the number of nodes per sector and handle leftovers
        num_sectors = len(sectors)
        base_nodes_per_sector = self.total_num_sensor_nodes // num_sectors
        extra_nodes = self.total_num_sensor_nodes % num_sectors  # Leftover nodes to distribute

        robot_id = 0  # Unique ID for each robot

        # Distribute nodes to each sector
        for i, sector in enumerate(sectors):
            x_start, x_end, y_start, y_end = sector

            # Assign extra nodes to some sectors until leftovers are used up
            nodes_in_this_sector = base_nodes_per_sector + (1 if i < extra_nodes else 0)

            # Place nodes randomly within the sector, avoiding obstacles
            placed_nodes = 0
            max_attempts = 1000  # Avoid infinite loops if placement fails
            attempts = 0
            while placed_nodes < nodes_in_this_sector and attempts < max_attempts:
                x = np.random.uniform(x_start, x_end)
                y = np.random.uniform(y_start, y_end)
                if self.is_valid_position(x, y):
                    # Create a Robot instance for the valid position
                    robot = Robot(
                        id=robot_id,
                        position=(x, y),
                        sector=sector,
                        orientation=(0, 0),  # Default orientation
                        power_level=np.random.uniform(50, 100)  # Random initial power level
                    )
                    self.robots.append(robot)
                    robot_id += 1
                    placed_nodes += 1
                attempts += 1

            if attempts >= max_attempts:
                print(f"Warning: Could not place all nodes in sector {sector}.")

        return self.robots