import numpy as np
import scipy.ndimage as ndimage

class FrontierIdentification:
    def __init__(self, map_height, map_width, matrix_height=100, matrix_width=100, alpha=1, beta=1, Imax=8, Lmax=None, hub=None, robot=None):
        self.map_height = map_height
        self.map_width = map_width
        self.matrix_height = matrix_height
        self.matrix_width = matrix_width
        self.map_matrix = np.zeros((self.matrix_height, self.matrix_width))
        self.frontier_set = []
        self.information_gain = []
        self.path_length = []
        self.cost_function = []
        self.optimal_frontier = None
        self.alpha = alpha
        self.beta = beta
        self.Imax = Imax
        self.Lmax = Lmax if Lmax else np.sqrt(self.matrix_height ** 2 + self.matrix_width ** 2)
        self.Hub = hub
        self.Robot = robot

    def update(self):
        self.update_map_matrix()
        self.update_frontier_set()
        self.find_information_gain()
        self.find_path_length()
        self.find_cost_function()
        self.find_optimal_frontier()

    def conv_map_to_matrix(self, x_map, y_map):
        j_matrix = min(max(round((x_map / self.map_width) * (self.matrix_width - 1)), 0), self.matrix_width - 1)
        i_matrix = min(max((self.matrix_height - 1) - round((y_map / self.map_height) * (self.matrix_height - 1)), 0), self.matrix_height - 1)
        return [i_matrix, j_matrix]

    def conv_matrix_to_map(self, i_matrix, j_matrix):
        x_map = (j_matrix / (self.matrix_width - 1)) * self.map_width
        y_map = (1 - (i_matrix / (self.matrix_height - 1))) * self.map_height
        return [x_map, y_map]

    def update_map_matrix(self):
        for robot in self.Hub.robots:
            for point in robot.estimate_history:
                try:
                    [i, j] = self.conv_map_to_matrix(point[0, 0], point[1, 0])
                    if 0 <= i < self.matrix_height and 0 <= j < self.matrix_width:
                        self.map_matrix[i, j] = 1
                except IndexError:
                    continue

        for point in self.Hub.collisions:
            try:
                [i, j] = self.conv_map_to_matrix(point[0], point[1])
                if 0 <= i < self.matrix_height and 0 <= j < self.matrix_width:
                    self.map_matrix[i, j] = 2
            except IndexError:
                continue

    def update_frontier_set(self):
        explored = self.map_matrix == 1
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        frontier_candidates = ndimage.convolve(explored.astype(int), kernel, mode='constant', cval=0)
        frontier_mask = (frontier_candidates > 0) & explored
        self.frontier_set = list(zip(*np.nonzero(frontier_mask)))

    def find_information_gain(self):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        gain_matrix = ndimage.convolve((self.map_matrix == 0).astype(int), kernel, mode='constant', cval=0)
        self.information_gain = [gain_matrix[i, j] for i, j in self.frontier_set]

    def find_path_length(self):
        self.path_length = []
        robot_location = self.Hub.robots[self.Robot.id].estimate_history[-1]
        robot_location = self.conv_map_to_matrix(robot_location[0, 0], robot_location[1, 0])
        for frontier_point in self.frontier_set:
            distance = np.sqrt((robot_location[0] - frontier_point[0]) ** 2 + (robot_location[1] - frontier_point[1]) ** 2)
            self.path_length.append(distance)

    def find_cost_function(self):
        IG = np.array(self.information_gain)
        PL = np.array(self.path_length)
        self.cost_function = (-1 * self.alpha * IG / self.Imax) + (self.beta * PL / self.Lmax)
        self.cost_function = list(self.cost_function)

    def find_optimal_frontier(self):
        if not self.frontier_set:
            self.optimal_frontier = None
            return
        i_min = np.argmin(self.cost_function)
        self.optimal_frontier = self.frontier_set[i_min]
