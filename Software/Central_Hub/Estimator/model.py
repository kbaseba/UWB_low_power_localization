import numpy as np

from .system import System

class RobotDynamics(System):
    """
    Class for simulating 2D robot dynamics with constant velocity.
    """
    def __init__(self, dt, Q, R):
        self.dt = dt  # Time step
        self.Φ = np.zeros((4, 4))  # State transition matrix
        self.B = np.array([
            [0],     # No control input affects x
            [0],     # No control input affects y
            [1],    # Angular velocity affects orientation
            [0]      # No control input affects velocity
        ])
        self.H = np.array([
            [1, 0, 0, 0],  # Measure x position
            [0, 1, 0, 0]   # Measure y position
        ])
        super().__init__(Φ=self.Φ, B=self.B, H=self.H, Q=Q, R=R)

    def compute_A(self, v, theta):
        """
        Compute the state transition matrix Φ based on velocity and orientation.
        """
        return np.array([
            [1, 0, -v * np.sin(theta) * self.dt, np.cos(theta) * self.dt],
            [0, 1, v * np.cos(theta) * self.dt, np.sin(theta) * self.dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def update_matrices(self, v, theta):
        """
        Update Φ dynamically based on current velocity and orientation.
        """
        self.Φ = self.compute_A(v, theta)