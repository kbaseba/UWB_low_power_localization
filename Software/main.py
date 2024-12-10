import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from simulator import Simulator
from testbench_tools import simulation_configuration_setup
import numpy as np

# GUI Application
class SimulatorGUI:
    def __init__(self, root):
        #Initialize tkinter root
        self.root = root
        self.root.title("Simulator GUI")
        
        # Settings frame
        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack(side=tk.LEFT)#, fill=tk.Y)

        # Control Buttons
        tk.Button(self.settings_frame, text="Start", command=self.start_simulator).pack()
        tk.Button(self.settings_frame, text="Restart", command=self.restart_simulator).pack()
        
        # Plot Frame
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(side=tk.RIGHT)#, fill=tk.BOTH, expand=True)
        self.figure, (self.ax1,self.ax2,self.ax3) = plt.subplots(1,3, figsize=(15,5))
        self.canvas = FigureCanvasTkAgg(self.figure, self.plot_frame)
        self.canvas.get_tk_widget().pack()#fill=tk.BOTH, expand=True)
    
    def start_simulator(self):
        try:
            # Get simulation settings
            map_width, map_height, num_obstacles, light_variation, num_sectors, total_num_sensor_nodes, node_range, random_seed, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R = simulation_configuration_setup()
            np.random.seed(random_seed)

            # Initialize the simulator
            self.simulator = Simulator(map_width, map_height, num_obstacles, light_variation, num_sectors, 
                                    total_num_sensor_nodes, node_range, threshold, duty_cycle, efficacy, 
                                    motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R)
            #self.simulator.axes = self.ax

            # Start animation
            self.animation = ani.FuncAnimation(self.figure, self.simulator.update, frames=100, interval=200)
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start simulator: {e}")
    
    def restart_simulator(self):
        if self.animation:
            self.animation.event_source.stop()
        self.start_simulator()


if __name__ == "__main__":
    root = tk.Tk()
    app = SimulatorGUI(root)
    root.mainloop()
