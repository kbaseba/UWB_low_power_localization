# Imports

import numpy as np
from Devices.hub import Hub
from Sensor_Nodes.robot import Robot
from SwarmCoordination.frontier_identification import FrontierIdentification

class PotentialFieldComputation:
    def _init_(self, FrontierIdentification, c=10, delta=0.001, phi_num=1, Hub, Robot):
        self.FrontierIdentification = FrontierIdentification
        self.FrontierIdentification.update(self.FrontierIdentification)
        self.optimal_frontier = self.FrontierIdentification.optimal_frontier
        self.c = c
        self.delta = delta
        self.phi_num = phi_num
        self.num_obs = self.find_num_obs(self)
        self.F_goal = np.array([0,0])
        self.F_boundary = np.array([0,0])
        self.F_obstacle = np.array([0,0])
        self.F_net = np.array([0,0])
        self.theta = 0
        self.Hub = Hub
        self.Robot = Robot
    
    def update(self):
        self.find_attractive_force(self)
        self.find_boundary_force(self)
        self.find_obstacle_force(self)
        self.find_next_direction(self)
    
    def find_num_obs(self):
        return len(self.Hub.collisions)

    def find_attractive_force(self):
        robot_location = self.Hub.robots[self.Robot.id].estimate_history[-1]
        goal_point = self.FrontierIdentification.conv_matrix_to_map(self.optimal_frontier[0],self.optimal_frontier[1])
        Fx_goal = (-self.c/np.sqrt((robot_location[0]-goal_point[0])*2 + (robot_location[1]-goal_point[1])2))(robot_location[0]-goal_point[0])
        Fy_goal = (-self.c/np.sqrt((robot_location[0]-goal_point[0])*2 + (robot_location[1]-goal_point[1])2))(robot_location[1]-goal_point[1])
        self.F_goal[0] = Fx_goal
        self.F_goal[1] = Fy_goal
    
    def find_boundary_force(self):
        robot_location = self.Hub.robots[self.Robot.id].estimate_history[-1]
        Fx_left = 1/((delta + (robot_location[0]-0))**2)
        Fx_right = -1/((delta + (self.FrontierIdentification.map_width-robot_location[0]))**2)
        Fy_bottom = 1/((delta + (robot_location[1]-0))**2)
        Fy_top = -1/((delta + (self.FrontierIdentification.map_height-robot_location[1]))**2)
        self.F_boundary[0] = Fx_left + Fx_right
        self.F_boundary[1] = Fy_bottom + Fy_top
    
    def find_obstacle_force(self):
        robot_location = self.Hub.robots[self.Robot.id].estimate_history[-1]
        phi_obs = np.zeros(self.num_obs)
        phi_max = -np.inf
        i_max = -1

        for i in range(self.num_obs):
            phi_obs[i] = self.phi_num/(1+np.sqrt((robot_location[0]-self.Hub.collisions[i][0])*2 + (robot_location[1]-self.Hub.collisions[i][1])*2))
            if(phi_obs[i] > phi_max):
                phi_max = phi_obs[i]
                i_max = i

        Fx_obstacle = (phi_max/(1+np.sqrt((robot_location[0]-self.Hub.collisions[i_max][0])*2 + (robot_location[1]-self.Hub.collisions[i_max][1])2))2)(1/np.sqrt((robot_location[0]-self.Hub.collisions[i_max][0])*2 + (robot_location[1]-self.Hub.collisions[i_max][1])2))(robot_location[0]-self.Hub.collisions[i_max][0])
        Fy_obstacle = (phi_max/(1+np.sqrt((robot_location[0]-self.Hub.collisions[i_max][0])*2 + (robot_location[1]-self.Hub.collisions[i_max][1])2))2)(1/np.sqrt((robot_location[0]-self.Hub.collisions[i_max][0])*2 + (robot_location[1]-self.Hub.collisions[i_max][1])2))(robot_location[1]-self.Hub.collisions[i_max][1])
        self.F_obstacle[0] = Fx_obstacle
        self.F_obstacle[1] = Fy_obstacle

    def find_next_direction(self):
        self.F_net = self.F_goal + self.F_boundary + self.F_obstacle
        self.theta = np.arctan(self.F_net[1]/self.F_net[0])
        self.Robot.orientation = (180/np.pi)*self.theta