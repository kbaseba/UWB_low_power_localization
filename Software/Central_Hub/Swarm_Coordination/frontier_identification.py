# Importing Libraries
import numpy as np

class FrontierIdentification:
    def __init__(self, map_height, map_width, matrix_height = 100, matrix_width = 100, alpha = 1, beta = 1, Imax = 1, Lmax = 1, hub = None, robot = None):
        self.map_height = map_height
        self.map_width = map_width
        self.matrix_height = matrix_height
        self.matrix_width = matrix_width
        self.map_matrix = np.zeros((self.matrix_height,self.matrix_width))
        self.frontier_set = []
        self.information_gain = []
        self.path_length = []
        self.cost_function = []
        self.optimal_frontier = ()
        self.alpha = alpha
        self.beta = beta
        self.Imax = 8
        self.Lmax = np.sqrt(self.matrix_height*2 + self.matrix_width*2)
        self.Hub = hub
        self.Robot = robot
    
    def update(self):
        self.update_map_matrix()
        self.update_frontier_set()
        self.find_information_gain()
        self.find_path_length()
        self.find_cost_function()
        self.find_optimal_frontier()

    def conv_map_to_matrix(self, x_map,y_map):
        j_matrix = round((x_map/self.map_width)*(self.matrix_width - 1))
        i_matrix = (self.matrix_height - 1) - round((y_map/self.map_height)*(self.matrix_height - 1))
        return [i_matrix,j_matrix]

    def conv_matrix_to_map(self, i_matrix, j_matrix):
        x_map = (j_matrix/(self.matrix_width - 1))*self.map_width
        y_map = (1-(i_matrix/(self.matrix_height - 1)))*self.map_height
        return [x_map,y_map]

    def update_map_matrix(self):
        for robot in self.Hub.robots:
            for point in robot.estimate_history:
                [i,j] = self.conv_map_to_matrix(point[0,0],point[1,0])
                self.map_matrix[i,j] = 1

        for point in self.Hub.collisions:
            [i,j] = self.conv_map_to_matrix(point[0],point[1])
            self.map_matrix[i,j] = 2
    
    def update_frontier_set(self):
        for i in range(self.matrix_height):
            for j in range(self.matrix_width):
                
                if(self.map_matrix[i,j] == 1):
                    
                    flag = 0
                    
                    for p in [-1,0,1]:
                        for q in [-1,0,1]:
                            if(p==0 and q==0):
                                continue
                            if((i+p >= 0) and (i+p <= self.matrix_height-1) and (j+q >= 0) and (j+q <= self.matrix_width-1)):
                                if(self.map_matrix[i+p,j+q] == 0):
                                    flag = 1
                                    break
                    
                    if(flag == 1):
                        self.frontier_set.append((i,j))
    
    def find_information_gain(self):
        self.information_gain = [0 for _ in range(len(self.frontier_set))]
        for i in range(len(self.frontier_set)):
            frontier_point = self.frontier_set[i]
            i_frontier = frontier_point[0]
            j_frontier = frontier_point[1]
            neighbour_count = 0
            for p in [-1,0,1]:
                for q in [-1,0,1]:
                    if(p==0 and q==0):
                        continue
                    if((i_frontier+p >= 0) and (i_frontier+p <= self.matrix_height-1) and (j_frontier+q >= 0) and (j_frontier+q <= self.matrix_width-1)):
                        if(self.map_matrix[i_frontier+p,j_frontier+q] == 0):
                            neighbour_count += 1
            
            self.information_gain[i] = neighbour_count

    def find_path_length(self):
        self.path_length = [0 for _ in range(len(self.frontier_set))]
        for i in range(len(self.frontier_set)):
            frontier_point = self.frontier_set[i]
            robot_location = self.Hub.robots[self.Robot.id].estimate_history[-1]
            robot_location = self.conv_map_to_matrix(robot_location[0,0],robot_location[1,0])
            self.path_length[i] = np.sqrt((robot_location[0]-frontier_point[0])*2 + (robot_location[1]-frontier_point[1])*2)
    
    def find_cost_function(self):
        self.cost_function = np.zeros(len(self.frontier_set))
        IG = np.array(self.information_gain)
        PL = np.array(self.path_length)
        self.cost_function = (-1*self.alpha*IG/self.Imax) + (self.beta*PL/self.Lmax)
        self.cost_function = list(self.cost_function)
    
    def find_optimal_frontier(self):
        CF_min = np.inf
        i_min = -1
        for i in range(len(self.cost_function)):
            if(self.cost_function[i] < CF_min):
                CF_min = self.cost_function[i]
                i_min = i

        self.optimal_frontier = self.frontier_set[i_min]