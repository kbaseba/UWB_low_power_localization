import numpy as np
from .system import System

class RobotDynamics(System):
    """
    Class for simulating 2D robot dynamics with constant velocity.
    """
    def __init__(self, dt, Q, R):
        # Validate dt
        if dt <= 0:
            raise ValueError(f"Time step dt must be positive, got {dt}")
        self.dt = dt  # Time step

        # Initialize state transition matrix Φ (identity for initial state)
        self.Φ = np.eye(4)

        # Control matrix B
        self.B = np.array([
            [0],     # No control input affects x
            [0],     # No control input affects y
            [1],     # Angular velocity affects orientation
            [0]      # No control input affects velocity
        ])

        # Observation matrix H
        self.H = np.array([
            [1, 0, 0, 0],  # Measure x position
            [0, 1, 0, 0]   # Measure y position
        ])

        # Initialize System class with matrices and noise covariances
        super().__init__(Φ=self.Φ, B=self.B, H=self.H, Q=Q, R=R)

    def compute_A(self, v, theta):
        """
        Compute the state transition matrix Φ based on velocity and orientation.
        :param v: Current velocity (scalar).
        :param theta: Current orientation in radians (scalar).
        :return: State transition matrix Φ.
        """
        # Validate inputs
        if not np.isscalar(v):
            raise ValueError(f"Expected scalar for v, got {type(v)}")
        if not np.isscalar(theta):
            raise ValueError(f"Expected scalar for theta, got {type(theta)}")

        # Compute the state transition matrix
        return np.array([
            [1, 0, -v * np.sin(theta) * self.dt, np.cos(theta) * self.dt],
            [0, 1, v * np.cos(theta) * self.dt, np.sin(theta) * self.dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def update_matrices(self, v, theta):
        """
        Update Φ dynamically based on current velocity and orientation.
        :param v: Current velocity (scalar).
        :param theta: Current orientation in radians (scalar).
        """
        self.Φ = self.compute_A(v, theta)
