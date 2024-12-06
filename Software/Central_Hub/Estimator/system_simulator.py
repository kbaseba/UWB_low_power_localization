import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import os

from .model import RobotDynamics
from .plant import Plant

class SystemSimulator:
    def __init__(self, dt, Q, R, x0, noisy):
        # Model initialization
        self.model = RobotDynamics(dt, Q, R)

        # Plant initialization
        self.plant = Plant(self.model, x0, noisy)

        self.x0 = x0


    def update(self, u, v, theta, x̂_: ndarray = None) -> ndarray:
        self.model.update_matrices(v, theta)
        return self.plant.update(u, x̂_)