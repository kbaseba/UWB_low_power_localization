import numpy as np
from Devices.hub import Hub
from Sensor_Nodes.robot import Robot
from SwarmCoordination.frontier_identification import FrontierIdentification

class PotentialFieldComputation:
    def __init__(self, FrontierIdentification, c=1, delta=0.001, phi_max=10, Hub, Robot):
        self.FrontierIdentification = FrontierIdentification
        self.FrontierIdentification.update(self.FrontierIdentification)
        self.optimal_frontier = self.FrontierIdentification.optimal_frontier
        self.Hub = Hub
        self.Robot = Robot
    
    def update(self):

    
    def find_attractive_force(self):
        

# Parameters required:
    # c = 1
    # delta = 0.001
    # phi_max = 10
    # num_obs
    # (x_goal,y_goal)
    # xb1, xb2, yb1, yb2
    # (x_obs,y_obs)[k]
    # Velocity Magnitude v0
    # dt -> time step

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
