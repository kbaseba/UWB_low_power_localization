# Imports
from Devices.hub import Hub
from Devices.anchor import Anchor
from Devices.robot import Robot
from map_creation import Map
import random, time

# Class comment
"""
The simulator will
1. Generate the map
2. Generate the anchors and place them at vertices of the map
3. Generate the robots and place them randomly throughout the map (need to implement obstacle avoidance)
4. Update the hub, then update the robots
"""
class Simulator:
    def __init__(self, num_robots=4, map_dimensions = [100,100]):
        #Generate the map
        self.map_dimensions = map_dimensions
        self.map = Map(width=self.map_dimensions[0], height=self.map_dimensions[1], num_obstacles=5, light_variation=True)
        
        #Generating anchors and placing at 3 vertices of map
        self.anchors = []
        vertices = [(0,0),(0,map_dimensions[0]),(map_dimensions[1],0)]
        for vertex in vertices:
            anchor = Anchor(position=vertex)
            self.addAnchor(anchor)

        #Generating robots at random positions in map that don't intersect obstacles
        self.robots = []
        for i in range(num_robots):
            #Randomly choosing a position, making sure that it doesn't intersect any obstacles
            pos = (random.randint(0,self.map_dimensions[0]),random.randint(0,self.map_dimensions[1]))
            while self.map._check_overlap("circle", pos[0],pos[1],0.5):
                print('Position intersects obstacle, retrying...')
                pos = (random.randint(0,self.map_dimensions[0]),random.randint(0,self.map_dimensions[1]))
            robot = Robot(id=i, position=pos)
            robot.update(map=self.map)
            self.addRobot(robot)

        #Generating hub
        self.Hub = Hub(self.anchors, self.robots)
        
        #Plotting the map
        self.map.plot_map(self.robots)

        pass
    
    #Function to add anchors to simulation
    def addAnchor(self, anchor):
        self.anchors.append(anchor)
        pass
    #Function to add robots to simulation
    def addRobot(self,robot):
        self.robots.append(robot)
        pass

    #Status to check simulator
    def printStatus(self):
        #Printing anchors
        for anchor in self.anchors:
            print(f"Anchor position: {anchor.position}")
        #Printing robot positions
        for robot in self.robots:
            print(f"Robot ID: {robot.id}")
            print(f"\tPosition: {robot.position}")

    def update(self):
        #Update Hub
        self.Hub.update()
        #Update robots
        for robot in self.robots:
            robot.update(self.map)
        pass

if __name__ =='__main__':
    #Creating simulator instance
    simulator = Simulator()
    simulator.printStatus()
    #Initializing time-step
    t = 0
    time_unit = 0.5
    while True:
        simulator.update()
        time.sleep(time_unit)
        t += 1
        print(f"Time step: {t}, time: {time_unit*t}\t")