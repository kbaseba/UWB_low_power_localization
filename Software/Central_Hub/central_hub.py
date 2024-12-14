# Imports
import numpy as np

from .Sector_Assignment.sector_assignment import SectorAssignment
from .Leader_Selection.leader_selection import LeaderSelection
from .update_sectors import UpdateSectors
from .Estimator.estimator import Estimator
from .mapping import Mapping
from .Swarm_Coordination.swarm_coordination import SwarmCoordination
from .map_accuracy import MapAccuracy

# Class comment
class CentralHub:
    def __init__(self, map, num_sectors, total_num_sensor_nodes, node_range, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R):
        self.map = map
        self.leader_nodes = None
        self.sector_assignment = SectorAssignment(self.map.width, self.map.height, num_sectors, total_num_sensor_nodes, node_range, self.map.obstacles, 
                                                  threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum, dt, Q, R)
        self.leader_selection = LeaderSelection()
        
        self.sectors, self.hub = self.sector_assignment.update()
        self.update_sectors = UpdateSectors(self.sectors, self.hub)

        self.estimators = [Estimator(dt, Q, R, np.array([[robot.position[0]], [robot.position[1]], [robot.orientation], [1.0]])) for robot in self.hub.robots]
        self.mapping = Mapping(self.hub)
        self.swarm_coordination = SwarmCoordination(self.hub)

        self.map_accuracy = MapAccuracy(self.hub, self.map)
        
    def update(self, frame=None):
        self.update_sectors.update()    # Update the sector for each non-leader based on current position
        self.leader_selection.update(self.hub)

        for robot in self.hub.robots:
            if robot.mode == "active":
                robot.move(self.map, self.hub.robots)

        for robot in self.hub.robots:
            robot.update(self.map, self.hub.robots)

        self.hub.receiveData()
        self.mapping.uwb_update()
        self.hub.update()
        
        for i, estimator in enumerate(self.estimators):
            
            if self.hub.robots[i].just_localized == True:
                self.hub.robots[i].just_localized = False
                x̂, P, r, A = estimator.update(u=np.array((self.hub.robots[i].orientation % 360) * (np.pi / 180)).reshape(1, 1), z=np.array(self.hub.robots[i].position).reshape(2, 1))
            else:
                x̂, P, r, A = estimator.update(u=np.array((self.hub.robots[i].orientation % 360) * (np.pi / 180)).reshape(1, 1), z=None)
            
            self.hub.robots[i].estimate_history.append(x̂)

        self.mapping.low_power_update()
        self.swarm_coordination.update(self.map)


        # Extract robot positions
        sensor_node_positions = [robot.position for robot in self.hub.robots]

        # Extract anchor positions
        anchor_position = [anchor.position for anchor in self.hub.anchors]

        # Extract hub position
        hub_position = self.hub.position

        # Update the map
        self.map.update(sectors=self.sectors, robots=self.hub.robots, hub=self.hub, sensor_node_positions=sensor_node_positions, anchor_positions=anchor_position, hub_position=hub_position, map_accuracy=self.map_accuracy)


