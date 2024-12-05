# Imports
from Devices.hub import Hub
from Devices.anchor import Anchor
from Devices.robot import Robot
from map_creation import Map
import random

# Class comment
class Simulator:
    def __init__(self, num_Robots=4, map_dimensions = [100,100]):
        #Generate the map
        self.map_dimensions = map_dimensions
        self.map = Map(width=self.map_dimensions[0], height=self.map_dimensions[1], num_obstacles=5, light_variation=True)
        
        #Generating hub, anchors, and robots
        self.Hub = Hub()
        self.anchors = []
        self.robots = []
        #Adding 3 anchors at 3 vertices of map
        vertices = [(0,0),(0,map_dimensions[0]),(map_dimensions[1],0)]
        for vertex in vertices:
            anchor = Anchor(position=vertex)
            self.addAnchor(anchor)
        
        #Adding robots at random positions
        for i in range(num_Robots):
            robot = Robot(id=i, position=(random.randint(0,self.map_dimensions[0]),random.randint(0,self.map_dimensions[1])))
            self.addRobot(robot)
        
        

        pass
    
    #Function to add anchors
    def addAnchor(self, anchor):
        self.anchors.append(anchor)
        pass

    #Function to add robots
    def addRobot(self,robot):
        self.robots.append(robot)
        pass

    def update(self):
        self.Hub.update()
        for robot in self.robots:
            robot.update()
        pass

    def printSim(self):
        print(f"Robot positions: {[robot.position for robot in self.robots]}\n Anchors: {[anchor.position for anchor in self.anchors]}")

if __name__ =='__main__':
    simulator = Simulator()
    simulator.printSim()
    while True:
        simulator.update()