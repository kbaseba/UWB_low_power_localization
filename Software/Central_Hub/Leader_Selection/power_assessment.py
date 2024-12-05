# Imports

# Class comment
class PowerAssessment:
    def __init__(self):
        self.current_leaders = {}  # Tracks the current leader for each sector

    def update(self, robots):
         # Group robots by sector boundaries
        sector_robots = {}
        for robot in robots:
            if robot.sector not in sector_robots:
                sector_robots[robot.sector] = []
            sector_robots[robot.sector].append(robot)

        # Update leaders for each sector
        self.current_leaders = {}
        for sector_coords, robots_in_sector in sector_robots.items():
            # Get the upper power threshold from any robot (all are the same)
            upper_threshold = robots_in_sector[0].power_threshold[1] if robots_in_sector else None

            # Filter robots above the upper power threshold
            eligible_robots = [
                robot for robot in robots_in_sector if robot.power_level > upper_threshold
            ]

            if eligible_robots:
                # Select the robot with the highest power as the leader
                leader = max(eligible_robots, key=lambda r: r.power_level)
                leader.role = "leader"  # Assign leader role
                self.current_leaders[sector_coords] = leader.id
            else:
                # Clear leader if no eligible robots
                self.current_leaders[sector_coords] = None

                # Reset role for all robots in this sector
                for robot in robots_in_sector:
                    if robot.role == "leader":
                        robot.role = "non-leader"

        return self.current_leaders