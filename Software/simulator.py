import numpy as np

from testbench_tools import simulation_configuration_setup

from map_creation import Map
from Central_Hub.central_hub import CentralHub

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Class comment
class Simulator:
    def __init__(self, map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, 
                 node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R):
        self.map = Map(width=map_width, height=map_height, num_obstacles=num_obstacles, light_variation=light_variation)
        self.central_hub = CentralHub(self.map, num_sectors, total_num_sensor_nodes, node_range, 
                                      threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R)

    def update(self, frames=100, interval=200):
        """Create an animation of the map."""
        animation = FuncAnimation(self.map.fig, self.central_hub.update, frames=frames, interval=interval)
        plt.show()

        animation.save('animation.mp4', fps=30, dpi=300, writer='ffmpeg')

if __name__ == "__main__":
    # Load configuration from JSON file
    map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R = simulation_configuration_setup()

    # Set random seed for reproducibility
    np.random.seed(random_seed)

    simulator = Simulator(map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R)

    simulator.update()