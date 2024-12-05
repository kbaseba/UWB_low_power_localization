import numpy as np

from testbesnch_tools import simulation_configuration_setup

from map_creation import Map
from Central_Hub.central_hub import CentralHub
from Sensor_Nodes.sensor_nodes import SensorNodes

# Class comment
class Simulator:
    def __init__(self, map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range):
        self.map = Map(width=map_width, height=map_height, num_obstacles=num_obstacles, light_variation=light_variation)
        self.central_hub = CentralHub(self.map, num_sectors, total_num_sensor_nodes, node_range)
        # self.sensor_nodes = SensorNodes()

    def update(self):
        while True:
            self.central_hub.update()

if __name__ == "__main__":
    # Load configuration from JSON file
    map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed = simulation_configuration_setup()

    # Set random seed for reproducibility
    np.random.seed(random_seed)

    simulator = Simulator(map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range)

    simulator.update()