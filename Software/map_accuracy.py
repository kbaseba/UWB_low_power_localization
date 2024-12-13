import numpy as np

class MapAccuracy:
    def __init__(self, Hub, Map):
        self.Hub = Hub
        self.Map = Map
        self.accuracy = self.find_map_accuracy()
    
    def find_map_accuracy(self):
        
        count = 0
        num_collisions = 0

        for point in self.Hub.collisions:
            num_collisions += 1
            x_col = point[0]
            y_col = point[1]
            flag_count = 0

            for obs in self.Map.obstacles:

                if(obs[0] == "rectangle"):
                    obs_xmin = obs[1]
                    obs_ymin = obs[2]
                    obs_xmax = obs[1] + obs[3]
                    obs_ymax = obs[2] + obs[4]
                    if((x_col >= obs_xmin) and (x_col <= obs_xmax) and (y_col >= obs_ymin) and (y_col <= obs_ymax)):
                        flag_count += 1
                
                elif(obs[0] == "circle"):
                    obs_cx = obs[1]
                    obs_cy = obs[2]
                    obs_rad = obs[3]
                    if((x_col - obs_cx)**2 + (y_col - obs_cy)**2 <= (obs_rad)**2):
                        flag_count += 1

                elif(obs[0] == "polygon"):
                    obs_vertices = obs[1]
                    num_vertices = obs_vertices.shape[0]
                    inside_flag = False

                    for i in range(num_vertices):
                        v1 = obs_vertices[i]
                        v2 = obs_vertices[(i+1) % num_vertices]

                        if(y_col > min(v1[1],v2[1])):
                            if(y_col <= max(v1[1],v2[1])):
                                if(x_col <= max(v1[0],v2[0])):
                                    x_intersect = v1[0] + ((v2[0] - v1[0])/(v2[1]-v1[1]))*(y_col - v1[1])

                                    if((x_col <= x_intersect) or (v1[0] == v2[0])):
                                        inside_flag = not inside_flag
                    
                    flag_count = int(inside_flag)
                
                if(flag_count == 1):
                    count += 1
                    break
            
        return (count/num_collisions)*100