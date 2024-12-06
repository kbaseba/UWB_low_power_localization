import numpy as np
from shapely.geometry import Point, Polygon, box

from Sensor_Nodes.robot import Robot
from Devices.anchor import Anchor
from Devices.hub import Hub

# Class comment
class NodePlacement:
    """
    Strategically positions sensor nodes, UWB anchors, and the central hub
    within each sector to ensure effective localization, communication, and data collection.
    """
    def __init__(self, total_num_sensor_nodes, node_range, obstacles, map_width, map_height):
        self.total_num_sensor_nodes = total_num_sensor_nodes  # Total number of sensor nodes
        self.node_range = node_range  # Communication range of each node
        self.obstacles = obstacles  # List of obstacles on the map
        self.robots = []  # List of Robot objects
        self.anchors = []  # List of Anchor objects
        
        self.map_width = map_width
        self.map_height = map_height

    def update(self, sectors, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum):
        # Place robots in sectors
        robots = self.place_robots(sectors, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum)

        # Place anchors at the vertices of the map
        anchors = self.place_anchors()

        # Place the central hub at the center of the map
        hub = self.place_hub(anchors, robots)

        return hub


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

    def place_robots(self, sectors, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum):
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
                        orientation=30,  # Default orientation
                        power_level=np.random.uniform(50, 100),  # Random initial power level
                        threshold=threshold,
                        duty_cycle=duty_cycle,
                        efficacy=efficacy,
                        motor_power_consum=motor_power_consum,
                        velocity=velocity,
                        ble_power_consum=ble_power_consum,
                        uwb_power_consum=uwb_power_consum
                    )
                    self.robots.append(robot)
                    robot_id += 1
                    placed_nodes += 1
                attempts += 1

            if attempts >= max_attempts:
                print(f"Warning: Could not place all nodes in sector {sector}.")

        return self.robots
    
    def place_anchors(self):
        """
        Place four anchors at the corners of the map.
        """
        # Define the corners of the map using map_width and map_height
        corners = [
            (0, 0),  # Bottom-left
            (0, self.map_height),  # Top-left
            (self.map_width, 0),  # Bottom-right
            (self.map_width, self.map_height)  # Top-right
        ]

        self.anchors = []  # Reset the list of anchors
        for i, (x, y) in enumerate(corners):
            anchor = Anchor(id=i, position=(x, y))  # Create an Anchor instance
            self.anchors.append(anchor)

        return self.anchors

    def place_hub(self, anchors, robots):
        """
        Place a central hub at the geometric center of the map.
        """
        # Calculate the center of the map
        center_x = self.map_width / 2
        center_y = self.map_height / 2

        # Create the Hub instance
        hub = Hub(
            id=0,  # Assuming a single hub with ID 0
            position=(center_x, center_y),
            anchors=anchors,
            robots=robots
        )

        return hub