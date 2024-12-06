"""
ECE 209AS.1 COMPUTATIONAL ROBOTICS
Date: 12/05/2024
2D Random Walk Algorithm
Name: Renish Israel
UID: 606530590 
"""

import numpy as np

x = 0 # x-coordinate of the robot's position
y = 0 # y-coordinate of the robot's position
s = np.transpose(np.array([x,y])) # robot's state

# Parameters required:
    # num_dir
    # velocity magnitude v0
    # dt -> time step

# Trajectory
rand_dir_index = np.random.randint(0,num_dir)
theta = rand_dir_index * (2*np.pi/num_dir)
x = x + dt*(v0*np.cos(theta))
y = y + dt*(v0*np.sin(theta))