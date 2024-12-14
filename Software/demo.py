import tkinter as tk
from tkinter import messagebox
import json
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from simulator import Simulator
from testbench_tools import simulation_configuration_setup

# Function to update config.json based on GUI inputs
def update_config(entries, config_path):
    try:
        # Convert entries to appropriate JSON values
        config_data = {}
        for key, entry in entries.items():
            value = entry.get()
            # Determine type based on JSON structure
            if value.isdigit():
                config_data[key] = int(value)
            elif key == "H":
                config_data[key] = json.loads(value)
            elif value.replace('.', '', 1).isdigit():
                config_data[key] = float(value)
            elif value.lower() in ["true", "false"]:
                config_data[key] = value.lower() == "true"
            else:
                config_data[key] = value
        print(config_data)
        # Save the updated configuration to the file
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=4)
        #messagebox.showinfo("Success", "Configuration updated!")
        return config_data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update configuration: {e}")
        return None

# Function to start the simulation
def start_simulation(entries, config_path):

    update_config(entries, config_path)
    map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics = simulation_configuration_setup()
    np.random.seed(random_seed)
    simulator = Simulator(map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R, plot_metrics)
    
    if plot_metrics:
        simulator.run(plot_metrics)
    else:
        simulator.update()

# Function to restart the simulation
def restart_simulation():
    plt.close()

# GUI setup
def create_gui(config_path):
    # Load initial config
    with open(config_path, 'r') as f:
        config = json.load(f)
    # Initialize tkinter
    root = tk.Tk()
    root.title("Simulator GUI")

    # Input fields
    entries = {}
    non_shows = ["map_width", "map_height", "node_range", "velocity", "dt", "H"]
    for idx, (key, value) in enumerate(config.items()):
        if key not in non_shows:
            if "_" in key:
                tk.Label(root, text=key.replace("_", " ").title()).grid(row=idx, column=0, padx=10, pady=5)
            elif len(key)>4:
                tk.Label(root, text=key.title()).grid(row=idx, column=0, padx=10, pady=5)
            else:
                tk.Label(root, text=key).grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(root)
            entry.insert(0, str(value))
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entries[key] = entry
        else:
            entry = tk.Entry(root)
            entry.insert(0, str(value))
            entries[key] = entry


    # Buttons
    tk.Button(root, text="Start", command=lambda: start_simulation(entries, config_path)).grid(
        row=len(config), column=0, padx=10, pady=10)
    tk.Button(root, text="Restart", command=lambda: restart_simulation()).grid(
        row=len(config), column=1, padx=10, pady=10)

    # Run GUI
    root.mainloop()

# Entry point
if __name__ == "__main__":
    CONFIG_FILE = "config.json"
    config_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
    create_gui(config_path)