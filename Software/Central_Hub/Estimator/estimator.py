import os
import numpy as np
from numpy import ndarray, eye, mean, var, eye
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh, inv
from scipy.stats import shapiro, kstest
from statsmodels.stats.diagnostic import acorr_ljungbox

from .estimator_update import EstimatorUpdate
from .system_simulator import SystemSimulator

class Estimator:
    def __init__(self, dt, Q, R, x0):
        # Dynamic System Simulator initialization for state estimator
        self.SystemSimulator = SystemSimulator(dt, Q, R, x0, noisy=False)

        # state Estimator update initialization
        self.EstimatorUpdate = EstimatorUpdate(self.SystemSimulator.model, eye(self.SystemSimulator.model.Φ.shape[1]), x0)

        # Initialize the state estimate output from the update phase. this will be x̂(t-1)
        self.x̂_ = None
    
    
    def update(self, u: ndarray, z: ndarray):
        if self.x̂_ is None:
            v = 1.0
            theta = float(u[0, 0])
        else:
            v = float(self.x̂_[3][-1])
            theta = float(u[0, 0])

        # State estimate before the measurement update phase
        _x̂, ẑ = self.SystemSimulator.update(u, v, theta, self.x̂_)

        if z is not None:
            # State estimate after the measurement update phase (correction step)
            x̂, P, r, A = self.EstimatorUpdate.update(z, _x̂, ẑ)
        else:
            # No measurement: Skip correction, use predicted values
            x̂, P, r, A = _x̂, self.EstimatorUpdate._P, None, None

        # Update the state estimate output for the next iteration
        self.x̂_ = x̂
        
        return x̂, P, r, A
    

