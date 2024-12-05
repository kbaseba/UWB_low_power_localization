import numpy as np

# Class for dividing the map into sectors
class MapDivision:
    def __init__(self, map_width, map_height, num_sectors):
        self.map_width = map_width
        self.map_height = map_height
        self.num_sectors = num_sectors
        self.sectors = []  # List of tuples representing sector boundaries

    def update(self):
        """
        Divide the map into rectangular sectors.
        Each sector is represented by its boundaries: (x_start, x_end, y_start, y_end).
        """
        sector_width = self.map_width // int(np.sqrt(self.num_sectors))
        sector_height = self.map_height // int(np.sqrt(self.num_sectors))
        
        self.sectors = []
        for i in range(int(np.sqrt(self.num_sectors))):
            for j in range(int(np.sqrt(self.num_sectors))):
                x_start = i * sector_width
                x_end = x_start + sector_width
                y_start = j * sector_height
                y_end = y_start + sector_height
                self.sectors.append((x_start, x_end, y_start, y_end))
        return self.sectors