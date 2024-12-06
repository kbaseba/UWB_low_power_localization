# Imports
import numpy as np
from Devices.robot import Robot

# Class comment
class FrontierIdentification:
    def __init__(self, map_width, map_height, matrix_width, matrix_height, ):
        self.matrix_height = matrix_height
        self.matrix_width = matrix_width
        self.xstate =

    def update(self):
        pass

import numpy as np

x = xr # current x-coordinate of the robot's position
y = yr # current y-coordinate of the robot's position
s = np.transpose(np.array([x,y])) # robot's state

# Parameters required:
    # Grid Size m x n
    # Metric weights: alpha & beta
    # Normalization Parameters: Imax & Lmax

# Current Environment Map modelled as a matrix
M = np.zeros((m,n)) 

if(is_obstacle == True):
    M[xr,yr] = 2
else:
    M[xr,yr] = 1

# Frontier Set creation
F = []

for i in range(m):
    for j in range(n):
        
        if(M[i,j] == 1):
            
            flag = 0
            
            for p in [-1,0,1]:
                for q in [-1,0,1]:
                    if(p==0 and q==0):
                        continue
                    if((i+p >= 0) and (i+p <= m-1) and (j+q >= 0) and (j+q <= n-1)):
                        if(M[i+p,j+q] == 0):
                            flag = 1
            
            if(flag == 1):
                F.append((i,j))

# Calculate Information Gain and Path Length
IG = [0 for _ in range(len(F))]
PL = [0 for _ in range(len(F))]

for i in range(len(F)):
    f = F[i]
    xf = f[0]
    yf = f[1]
    
    PL[i] = np.sqrt((xr-xf)**2 + (yr-yf)**2) # Path Length
    
    count = 0
    for p in [-1,0,1]:
        for q in [-1,0,1]:
            if(p==0 and q==0):
                continue
            if((xf+p >= 0) and (xf+p <= m-1) and (yf+q >= 0) and (yf+q <= n-1)):
                if(M[xf+p,yf+q] == 0):
                    count += 1
    
    IG[i] = count

# Cost Function
IG = np.array(IG)
PL = np.array(PL)
CF = list(((-alpha/Imax)*IG) + ((beta/Lmax)*PL))

CF_min = np.inf
i_min = -1

for i in len(CF):
    if(CF[i] < CF_min):
        CF_min = CF[i]
        i_min = i

# Optimal Frontier
fopt = F[i_min]