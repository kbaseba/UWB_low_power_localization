import numpy as np

from testbench_tools import simulation_configuration_setup

from map_creation import Map
from Central_Hub.central_hub import CentralHub

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation

# Class comment
class Simulator:
    def __init__(self, map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, 
                 node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics):
        self.map = Map(plot_metrics, width=map_width, height=map_height, num_obstacles=num_obstacles, light_variation=light_variation)
        self.central_hub = CentralHub(self.map, num_sectors, total_num_sensor_nodes, node_range, 
                                      threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics)

    def update(self, frames=200, interval=200):
        """Create an animation of the map."""
        animation = FuncAnimation(self.map.fig, self.central_hub.update, frames=frames, interval=interval)
        # animation.save("animation.mp4",fps=30,dpi=300,writer="ffmpeg")
        #Setting position to the left
        #matplotlib.use("TkAgg")
        manager = plt.get_current_fig_manager()
        try:
            manager.window.wm_geometry("+1000+1000")  # Adjust X (horizontal) and Y (vertical) offsets
        except AttributeError:
            # For other backends like 'QtAgg', you may need to use a different method
            if hasattr(manager, "window"):
                manager.window.setGeometry(1000, 100, 800, 600)  # x, y, width, height
        plt.show()

    def run(self, plot_metrics, num_steps=1000):
        """Run the simulation without animation."""
        for _ in range(num_steps):
            self.central_hub.update(plot_metrics)  # Update logic for the simulation
            
        self.map.plot_metrics()

if __name__ == "__main__":
    # Load configuration from JSON file
    map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics = simulation_configuration_setup()

    # Set random seed for reproducibility
    np.random.seed(random_seed)

    simulator = Simulator(map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics)
    
    if plot_metrics:
        simulator.run(plot_metrics)
    else:
        simulator.update()