# Import


# Class
class UpdateSectors:
    def __init__(self, sectors, hub):
        self.sectors = sectors
        self.hub = hub

    def determine_sector(self, position):
        """
        Determine the sector a robot belongs to based on its position.
        
        :param position: Tuple of (x, y) coordinates representing the robot's position.
        :return: The sector boundaries the position belongs to, or None if no sector matches.
        """
        for sector_boundaries in self.sectors:
            x_start, x_end, y_start, y_end = sector_boundaries
            if x_start <= position[0] <= x_end and y_start <= position[1] <= y_end:
                return sector_boundaries
        return None  # No matching sector

    def update(self):
        """
        Update the sector assignments for all robots based on their current positions.
        
        :return: Dictionary mapping sector boundaries (tuples) to lists of robots currently in those sectors.
        """
        # Iterate through all robots in the hub
        for robot in self.hub.robots:
            if robot.role == "non-leader":
            # Determine the sector based on the robot's position
                robot.sector = self.determine_sector(robot.position)