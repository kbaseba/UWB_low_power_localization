"""
ECE 209AS.1 COMPUTATIONAL ROBOTICS
Date: 12/05/2024
Artificial Potential Field Algorithm
Name: Renish Israel
UID: 606530590 
"""

import numpy as np

x = 0 # x-coordinate of the robot's position
y = 0 # y-coordinate of the robot's position
s = np.transpose(np.array([x,y])) # robot's state

# Parameters required:
    # c = 1
    # delta = 0.001
    # phi_max = 10
    # num_obs
    # (x_goal,y_goal)
    # xb1, xb2, yb1, yb2
    # (x_obs,y_obs)[k]
    # Velocity Magnitude v0

# Attractive Potential
phi_goal = c*np.sqrt((x-x_goal)**2 + (y-y_goal)**2)

Fx_goal = (-c/np.sqrt((x-x_goal)**2 + (y-y_goal)**2))*(x-x_goal)
Fy_goal = (-c/np.sqrt((x-x_goal)**2 + (y-y_goal)**2))*(y-y_goal)

# Boundary Potential
Fx_left = 1/(delta + (x-xb1))**2
Fx_right = -1/(delta + (xb2-x))**2
Fy_top = -1/(delta + (yb1-y))**2
Fy_bottom = 1/(delta + (y-yb2))**2

# Obstacle Potential
phi_obs = np.zeros(num_obs)
phi_max = 0
i_max = 0

for i in range(num_obs):
    phi_obs[i] = phi_max/(1+np.sqrt((x-x_obs[i])**2 + (y-y_obs[i])**2))
    if(phi_obs[i] > phi_max):
        phi_max = phi_obs[i]
        i_max = i

phi_obs = phi_obs[i_max]

Fx_obs = (phi_max/(1+np.sqrt((x-x_obs[i_max])**2 + (y-y_obs[i_max])**2))**2)*(1/np.sqrt((x-x_obs[i_max])**2 + (y-y_obs[i_max])**2))*(x-x_obs[i_max])
Fy_obs = (phi_max/(1+np.sqrt((x-x_obs[i_max])**2 + (y-y_obs[i_max])**2))**2)*(1/np.sqrt((x-x_obs[i_max])**2 + (y-y_obs[i_max])**2))*(y-y_obs[i_max])

# Net Force
Fx_net = Fx_goal + Fx_left + Fx_right + Fx_obs
Fy_net = Fy_goal + Fy_left + Fy_right + Fy_obs

# Trajectory
theta = np.arctan(Fy_net/Fx_net)
x = x + dt*(v0*np.cos(theta))
y = y + dt*(v0*np.sin(theta))