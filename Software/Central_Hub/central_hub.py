# Imports

from .Sector_Assignment.sector_assignment import SectorAssignment
from .Leader_Selection.leader_selection import LeaderSelection
from .data_reception import DataReception
from .Estimator.estimator import Estimator
from .mapping import Mapping
from .Swarm_Coordination.swarm_coordination import SwarmCoordination

# Class comment
class CentralHub:
    def __init__(self, map, num_sectors, total_num_sensor_nodes, node_range):
        self.map = map
        self.leader_nodes = None
        self.sector_assignment = SectorAssignment(self.map.width, self.map.height, num_sectors, total_num_sensor_nodes, node_range, self.map.obstacles)
        self.leader_selection = LeaderSelection()
        self.sectors, self.hub = self.sector_assignment.update()

        self.data_reception = DataReception()
        self.estimator = Estimator()
        self.mapping = Mapping()
        self.swarm_coordination = SwarmCoordination()
        
    def update(self):
        self.leader_nodes = self.leader_selection.update(self.hub.robots)

        for robot in self.hub.robots:
            robot.move()

        for robot in self.hub.robots:
            robot.update()

        self.data_reception.update(self.hub.robots)
        self.estimator.update(self.hub.robots)
        self.mapping.update(self.hub.robots)
        self.swarm_coordination.update(self.hub.robots)


        


        

















        # Extract robot positions
        sensor_node_positions = [robot.position for robot in self.hub.robots]

        # Extract anchor positions
        anchor_position = [anchor.position for anchor in self.hub.anchors]

        # Extract hub position
        hub_position = self.hub.position

        # Step 3: Leader selection
        leader_selection = LeaderSelection()
        leader_nodes = leader_selection.update(self.hub.robots)

        # Step 5: Print leader nodes with their IDs and power levels
        print("Leader Nodes:")
        for sector, leader_id in leader_nodes.items():
            if leader_id is not None:
                # Find the corresponding robot object
                leader_robot = next(robot for robot in self.hub.robots if robot.id == leader_id)
                print(f"Sector: {sector}, Leader ID: {leader_robot.id}, Power Level: {leader_robot.power_level}")
            else:
                print(f"Sector: {sector}, No leader assigned")

        self.map.plot_map(sectors=self.sectors, sensor_node_positions=sensor_node_positions, anchor_positions=anchor_position, hub_position=hub_position)


