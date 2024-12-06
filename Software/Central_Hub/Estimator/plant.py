import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import os

from .system import System
from .plant_history import PlantHistory

class Plant:
    def __init__(self, s: System, x0: ndarray, noisy: bool):
        self.s = s
        self._x = x0
        self.noisy = noisy
        self._z, self._v = s.output(x0, noisy)
        self.h = PlantHistory([self._x], [], [self._z], [], [])


    def update(self, u: ndarray, x̂_: ndarray = None) -> ndarray:
        if x̂_ is None:
            # Use the actual state (for real-world simulation)
            x, z, w, v = self.s.update(self._x, u, self.noisy)
        else:
            # Use the estimated state x̂ (for estimator testing)
            x, z, w, v = self.s.update(x̂_, u, self.noisy)

        self.h.append(x, u, z, w, v)
        self._x, self._z = x, z
        
        return x, z