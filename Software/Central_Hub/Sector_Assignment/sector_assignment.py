from .map_division import MapDivision
from .node_placement import NodePlacement

# Class for assigning sectors and placing nodes
class SectorAssignment:
    def __init__(self, map_width, map_height, num_sectors, num_nodes, node_range, obstacles):
        self.map_division = MapDivision(map_width, map_height, num_sectors)
        self.node_placement = NodePlacement(num_nodes, node_range, obstacles)

    def update(self):
        """
        Perform sector division and node placement.
        """
        sectors = self.map_division.update()
        nodes = self.node_placement.update(sectors)
        return sectors, nodes