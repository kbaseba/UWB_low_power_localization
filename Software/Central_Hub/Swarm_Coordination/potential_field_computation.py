import numpy as np

from .frontier_identification import FrontierIdentification

class PotentialFieldComputation:
    def __init__(self, map, c=10, delta=0.001, phi_num=10, hub=None, robot=None):
        self.FrontierIdentification = FrontierIdentification(map_height=map.height, map_width=map.width, hub=hub, robot=robot)
        self.FrontierIdentification.update()
        self.optimal_frontier = self.FrontierIdentification.optimal_frontier
        self.c = c
        self.delta = delta
        self.phi_num = phi_num
        self.theta = 0.0
        self.Hub = hub
        self.Robot = robot
        self.num_obs = self.find_num_obs()
        self.F_goal = np.array([0.0, 0.0])
        self.F_boundary = np.array([0.0, 0.0])
        self.F_obstacle = np.array([0.0, 0.0])
        self.F_robot_repulsion = np.array([0.0, 0.0])
        self.F_net = np.array([0.0, 0.0])

    def update(self):
        self.find_attractive_force()
        self.find_boundary_force()
        self.find_obstacle_force()
        self.find_robot_repulsion_force()
        self.find_next_direction()

    def find_num_obs(self):
        return len(self.Hub.collisions)

    def find_attractive_force(self):
        if self.optimal_frontier is None:
            print("Error: Optimal frontier is None. Skipping attractive force calculation.")
            self.F_goal = np.array([0.0, 0.0])
            return
        
        robot_location = np.array(self.Hub.robots[self.Robot.id].estimate_history[-1]).flatten()[:2]
        goal_point = self.FrontierIdentification.conv_matrix_to_map(self.optimal_frontier[0], self.optimal_frontier[1])
        goal_point = np.array(goal_point).flatten()[:2]

        distance = np.linalg.norm(robot_location - goal_point)
        if distance == 0:
            distance = self.delta
        Fx_goal = (-self.c / distance) * (robot_location[0] - goal_point[0])
        Fy_goal = (-self.c / distance) * (robot_location[1] - goal_point[1])
        self.F_goal = np.array([Fx_goal, Fy_goal])

    def find_boundary_force(self):
        robot_location = np.array(self.Hub.robots[self.Robot.id].estimate_history[-1]).flatten()[:2]
        Fx_left = 1 / ((self.delta + (robot_location[0] - 0)) ** 2)
        Fx_right = -1 / ((self.delta + (self.FrontierIdentification.map_width - robot_location[0])) ** 2)
        Fy_bottom = 1 / ((self.delta + (robot_location[1] - 0)) ** 2)
        Fy_top = -1 / ((self.delta + (self.FrontierIdentification.map_height - robot_location[1])) ** 2)
        self.F_boundary = np.clip(np.array([Fx_left + Fx_right, Fy_bottom + Fy_top]), -1.0, 1.0)

    def find_obstacle_force(self):
        robot_location = np.array(self.Hub.robots[self.Robot.id].estimate_history[-1]).flatten()[:2]
        phi_obs = np.zeros(self.num_obs)
        for i, collision in enumerate(self.Hub.collisions):
            collision = np.array(collision).flatten()[:2]
            distance = np.linalg.norm(robot_location - collision)
            if distance == 0:
                continue
            phi_obs[i] = self.phi_num / (1 + distance)
        if not phi_obs.any():
            self.F_obstacle = np.array([0.0, 0.0])
            return
        i_max = np.argmax(phi_obs)
        phi_max = phi_obs[i_max]
        collision_point = np.array(self.Hub.collisions[i_max]).flatten()[:2]
        distance = np.linalg.norm(robot_location - collision_point)
        if distance == 0:
            distance = self.delta
        Fx_obstacle = (phi_max / ((1 + distance) ** 2)) * (1 / (self.delta + distance)) * (robot_location[0] - collision_point[0])
        Fy_obstacle = (phi_max / ((1 + distance) ** 2)) * (1 / (self.delta + distance)) * (robot_location[1] - collision_point[1])
        self.F_obstacle = np.clip(np.array([Fx_obstacle, Fy_obstacle]), -1.0, 1.0)

    def find_robot_repulsion_force(self):
        robot_location = np.array(self.Hub.robots[self.Robot.id].estimate_history[-1]).flatten()[:2]
        repulsion = np.array([0.0, 0.0])
        for other_robot in self.Hub.robots:
            if other_robot.id == self.Robot.id:
                continue
            other_location = np.array(other_robot.estimate_history[-1]).flatten()[:2]
            distance = np.linalg.norm(robot_location - other_location)
            if distance < self.delta or distance == 0:  # Avoid division by zero
                continue
            force = (1 / (distance ** 2)) * (robot_location - other_location) / distance
            repulsion += force
        self.F_robot_repulsion = np.clip(repulsion, -1.0, 1.0)

    def find_next_direction(self):
        self.F_net = self.F_goal + self.F_boundary + self.F_obstacle + self.F_robot_repulsion
        
        # Add random perturbation if net force is too small
        magnitude = np.linalg.norm(self.F_net)
        if magnitude < 1e-3:
            self.F_net += np.random.uniform(-0.1, 0.1, size=2)
        
        self.F_net = np.array(self.F_net).flatten()[:2]
        self.theta = np.arctan2(self.F_net[1], self.F_net[0])
        self.Robot.orientation = (180 / np.pi) * self.theta
