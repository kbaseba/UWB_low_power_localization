# Imports
import numpy as np

from Central_Hub.Estimator.system_simulator import SystemSimulator
from .sensor_nodes import SensorNodes
from .Instruction_execution.instruction_execution import InstructionExecution
from .Instruction_execution.move_robot import MoveRobot
from .power_harvest import PowerHarvest
from .transmit_data import TransmitData
from .uwb_localization import UWBLocalization


# This class represents a robot with various capabilities, including movement, data transmission,
# power harvesting, and role-based tasks. It integrates multiple components to simulate a robot's
# behavior in a dynamic environment.
class Robot:
    def __init__(self, dt, Q, R, id = 0, position = (0, 0), sector = 0, orientation = 0, power_level = 100, role = "non-leader", threshold = (10, 50), duty_cycle = 0, 
                 motor_power_consum = 0, velocity = 0, efficacy = 0, ble_power_consum = 0, uwb_power_consum = 0):
        """
        Initializes a robot instance with its components and initial state.

        Args:
            id (int): Unique identifier for the robot.
            position (tuple): Initial position of the robot (x, y).
            orientation (tuple): Initial orientation vector of the robot.
            power_level (float): Initial power level of the robot.
            role (str): Role assigned to the robot (e.g., "leader", "non-leader").
            power_threshold (tuple): Power threshold of entering and exiting low power mode.
            data_receiver (object): Instance responsible for receiving instructions.
            executor (object): Instance responsible for executing movement.
            sensors (object): Instance managing the robot's sensor nodes.
            power_harvester (object): Instance managing power harvesting.
            data_transmitter (object): Instance managing data transmission.
            uwb_transmitter (object): Instance managing UWB localization signals.
        """
        self.id = id  # Unique ID of the robot
        self.position = position  # (x, y) coordinates of the robot's position
        self.sector = sector # Sector of the robot
        self.orientation = orientation  # Orientation vector (dx, dy)
        self.power_level = power_level  # Remaining power level (max 100)
        self.role = role  # Role of the robot (e.g., leader/non-leader)
        self.mode = "active" # Mode of the robot (e.g., active/low power)
        self.power_threshold = threshold # Power Threshold for low power mode
        self.just_localized = False
        self.estimate_history = []
        self.velocity = velocity

        # Components responsible for specific robot tasks
        self.sensors = SensorNodes()
        self.power_harvester = PowerHarvest(efficacy)
        self.data_transmitter = TransmitData(ble_power_consum, duty_cycle)
        self.uwb_transmitter = UWBLocalization(uwb_power_consum)

        self.system_simulator = SystemSimulator(dt, Q, R, np.array([[self.position[0]], [self.position[1]], [self.orientation], [self.velocity]]), True)
        
        self.executor = InstructionExecution(self.system_simulator, MoveRobot(motor_power_consum, velocity))

    def move(self, map, robots):
        """
        Updates the robot's position based on its movement capabilities.
        This method triggers sensor updates and executes assigned tasks.
        """
        self.sensors.update(self, map, robots)  # Update sensor readings
        self.executor.update(self, map, robots)  # Execute movement

    def update(self, map, robots):
        """
        Updates the robot's state by refreshing sensor data, harvesting power,
        transmitting data, and handling UWB localization signals.
        """
        self.sensors.update(self, map, robots)  # Refresh sensor readings
        self.power_harvester.update(self)  # Harvest power based on light intensity
        self.data_transmitter.update(self)  # Handle data transmission
        self.uwb_transmitter.update(self)  # Activate or deactivate UWB localization
        # Check if the robot enters lower power mode from active
        if self.mode == "active" and self.power_level < self.power_threshold[0]:
            self.mode = "low power"
            # Inform the central hub of entering low power mode
            self.data_transmitter.state = True
            self.power_level -= self.data_transmitter.power_consum
            self.data_transmitter.data = {
                "id": self.id,
                "mode": self.mode,
                "power_level": self.power_level,
                "light_intensity": self.sensors.light_intensity,
                "button_sensor_state": self.sensors.button_sensor
            }
        elif self.mode == "low power" and self.power_level > self.power_threshold[1]:
            self.mode = "active"
            # Inform the central hub of exiting low power mode
            self.data_transmitter.state = True
            self.power_level -= self.data_transmitter.power_consum
            self.data_transmitter.data = {
                "id": self.id,
                "mode": self.mode,
                "power_level": self.power_level,
                "light_intensity": self.sensors.light_intensity,
                "button_sensor_state": self.sensors.button_sensor
            }