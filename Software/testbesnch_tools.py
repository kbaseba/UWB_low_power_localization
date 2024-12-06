import numpy as np
import json
import os

# Load configuration from JSON file
def load_config(config_path):
    config_path = os.path.join(os.path.dirname(__file__), config_path)
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

    threshold = (config["min_power_threshold"], config["max_power_threshold"])
    duty_cycle = config["duty_cycle"]
    efficacy = config["efficacy"]
    motor_power_consum = config["motor_power_consum"]
    velocity = config["velocity"]
    ble_power_consum = config["ble_power_consum"]
    uwb_power_consum = config["uwb_power_consum"]

    return map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum