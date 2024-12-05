import numpy as np
import json

# Load configuration from JSON file
def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)
    
def simulation_configuration_setup():
    config_path = "config.json"
    config = load_config(config_path)

    map_width = config["map_width"]
    map_height = config["map_height"]
    num_obstacles = config["num_obstacles"]
    light_variation = config["light_variation"]

    num_sectors = config["num_sectors"]
    total_num_sensor_nodes = config["total_num_sensor_nodes"]
    node_range = config["node_range"]

    random_seed = config["random_seed"]

    return map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed