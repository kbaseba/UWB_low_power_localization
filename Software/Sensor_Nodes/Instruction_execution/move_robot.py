# Imports
import math
import numpy as np

# This class moves the robot in its current orientation and updates its power level accordingly.
class MoveRobot:
    def __init__(self, motor_power_consum = 1, velocity = 0.1):
        """
        Initializes the movement system for the robot.

        Args:
            power_consum (float): Power consumed per movement step.
            velocity (float): Movement velocity per update.
        """
        self.motor_power_consum = motor_power_consum
        self.velocity = velocity
        self.state = True  # Indicates whether the robot can move.
    
    def update(self, robot, map, robots, system_simulator):
        """
        Updates the robot's position and power level.

        Args:
            robot (object): The robot object being updated.
            power_threshold (float): Power threshold for low power mode.
        """
        # Check if the robot is in low power mode
        if robot == "low power":
            return
        # Reduce power for movement
        robot.power_level -= self.motor_power_consum
        # Move forward if no collision is found
        if self.state:
            if robot.sensors.button_sensor:
                # Reverse movement
                # robot.position = (
                #     robot.position[0] - self.velocity * math.cos((robot.orientation/360)*2*math.pi),
                #     robot.position[1] - self.velocity * math.sin((robot.orientation/360)*2*math.pi)
                # )
                # robot.orientation = (robot.orientation + 180) % 360
                _, z = system_simulator.update(u=np.array((robot.orientation % 360) * (np.pi / 180)).reshape(1, 1), v=robot.velocity, theta=(robot.orientation % 360) * (np.pi / 180))
                robot.position = (
                    max(0, min(map.light_map.shape[0] - 1, z[0][0])),
                    max(0, min(map.light_map.shape[1] - 1, z[1][0]))
                )   
            
            else:
                # Forward movement
                # robot.position = (
                #     robot.position[0] + self.velocity * math.cos((robot.orientation/360)*2*math.pi),
                #     robot.position[1] + self.velocity * math.sin((robot.orientation/360)*2*math.pi)
                # )
                _, z = system_simulator.update(u=np.array((robot.orientation % 360) * (np.pi / 180)).reshape(1, 1), v=robot.velocity, theta=(robot.orientation % 360) * (np.pi / 180))
                robot.position = (
                    max(0, min(map.light_map.shape[0] - 1, z[0][0])),
                    max(0, min(map.light_map.shape[1] - 1, z[1][0]))
                )   

            # Update sensor readings after movement
            robot.sensors.update(robot, map, robots)
        

