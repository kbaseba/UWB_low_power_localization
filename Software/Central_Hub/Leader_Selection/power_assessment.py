# Imports

class PowerAssessment:
    def __init__(self):
        pass

    def update(self, hub):
        sector_robots = {}
        for robot in hub.robots:
            if robot.sector not in sector_robots:
                sector_robots[robot.sector] = []
            sector_robots[robot.sector].append(robot)

        for sector_coords, robots_in_sector in sector_robots.items():
            existing_leader = next((robot for robot in robots_in_sector if robot.role == "leader"), None)

            if existing_leader:
                continue

            upper_threshold = robots_in_sector[0].power_threshold[1]
            eligible_robots = [
                robot for robot in robots_in_sector if robot.power_level > upper_threshold
            ]
            if eligible_robots:
                # Select the robot with the highest power
                new_leader = max(eligible_robots, key=lambda r: r.power_level)
                new_leader_id = int(new_leader.id)
                hub.robots[new_leader_id].role = "leader"
