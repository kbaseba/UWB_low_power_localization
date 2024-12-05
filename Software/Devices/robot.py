# Imports

# This class represents a robot with various capabilities, including movement, data transmission,
# power harvesting, and role-based tasks. It integrates multiple components to simulate a robot's
# behavior in a dynamic environment.
class Robot:
    def __init__(self, id = 0, position = (0, 0), orientation = (0, 0), power_level = 100, role = "non-leader", power_threshold = (10, 50), data_receiver = None,
                  executor = None, sensors = None, power_harvester = None, data_transmitter = None, uwb_transmitter = None):
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
        self.orientation = orientation  # Orientation vector (dx, dy)
        self.power_level = power_level  # Remaining power level (max 100)
        self.role = role  # Role of the robot (e.g., leader/non-leader)
        self.mode = "active" # Mode of the robot (e.g., active/low power)
        self.power_threshold = power_threshold # Power Threshold for low power mode

         # Components responsible for specific robot tasks
        self.data_receiver = data_receiver
        self.executor = executor
        self.sensors = sensors
        self.power_harvester = power_harvester
        self.data_transmitter = data_transmitter
        self.uwb_transmitter = uwb_transmitter

    def move(self):
        """
        Updates the robot's position based on its movement capabilities.
        This method triggers sensor updates and executes assigned tasks.
        """
        self.sensors.update()  # Update sensor readings
        self.executor.update()  # Execute movement

    def update(self, map, instruction = None):
        """
        Updates the robot's state by refreshing sensor data, harvesting power,
        transmitting data, and handling UWB localization signals.
        """
        self.sensors.update(self, map)  # Refresh sensor readings
        self.power_harvester.update(self)  # Harvest power based on light intensity
        self.data_transmitter.update(self)  # Handle data transmission
        self.uwb_transmitter.update(self)  # Activate or deactivate UWB localization
        self.data_receiver.update(self, instruction)  # Parse and execute received instructions
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
                "button_sensor_state": self.senser_nodes.button_sensor
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
                "button_sensor_state": self.senser_nodes.button_sensor
            }