from .map_division import MapDivision
from .node_placement import NodePlacement

# Class for assigning sectors and placing nodes
class SectorAssignment:
    def __init__(self, map_width, map_height, num_sectors, num_nodes, node_range, obstacles, threshold, duty_cycle, efficacy, motor_power_consum, velocity, ble_power_consum, uwb_power_consum):
        self.map_division = MapDivision(map_width, map_height, num_sectors)
        self.node_placement = NodePlacement(num_nodes, node_range, obstacles, map_width, map_height)

        self.threshold = threshold
        self.duty_cycle = duty_cycle
        self.efficacy = efficacy
        self.motor_power_consum = motor_power_consum
        self.velocity = velocity
        self.ble_power_consum = ble_power_consum
        self.uwb_power_consum = uwb_power_consum

    def update(self):
        """
        Perform sector division and node placement.
        """
        sectors = self.map_division.update()
        hub = self.node_placement.update(sectors, self.threshold, self.duty_cycle, self.efficacy, self.motor_power_consum, self.velocity, self.ble_power_consum, self.uwb_power_consum) 
        return sectors, hub