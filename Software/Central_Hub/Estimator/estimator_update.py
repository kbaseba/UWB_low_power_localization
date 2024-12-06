import numpy as np
from numpy import ndarray, linalg, eye

from .system import System
from .estimator_history import EstimatorHistory

''' State_Estimator:

The state_estimator class was created based on the Standard Kalman Filter implementation
where the following functions were used (@ signifies dot product):

'''
class EstimatorUpdate:
    def __init__(self, s: System, P0: ndarray, x0: ndarray):
        self.s = s
        self._P = P0
        self.x0 = x0
        self.h = EstimatorHistory([self.x0], [self._P], [], [])
    
    
    # Only two inputs are allowed for state estimation u, and z and only update should be called
    # externally. Consolidated the predict and update steps into one function
    def update(self, z: ndarray, _x̂: ndarray, ẑ: ndarray) -> 'tuple[ndarray, ndarray]':
        ''' Predict Phase of Kalman Filter
        
            x[t] = A @ x[t-1] + B @ u[t-1]              (1) Computed within the plant
            P[t] = A @ P[t-1] @ A.T + Q                 (2)
            
        '''
        _P = self.s.Φ @ self._P @ self.s.Φ.T + self.s.Q
        ''' Update Phase of Kalman Filter
        
            K = P[t] @ H.T @ (H @ P[t] @ H.T + R)^-1    (4)
            x[t] = x[t] + K @ (z[t] - H @ x[t])         (5)
            P[t] = P[t] - K @ H @ P[t]                  (6)

        '''
        A = ((self.s.H @ _P @ self.s.H.T) + self.s.R)   # Residual covariance
        
        K = _P @ self.s.H.T @ linalg.inv(A)             # Kalman Gain
        r = z - ẑ                                       # Residual (innovation)
        x̂ = _x̂ + K @ (r)                                # Corrected state prediction
        P = _P - K @ self.s.H @ _P                      # Corrected prediction covariance 
        
        self._x, self._P = x̂, P                         # Update previous state
        self.h.append(x̂, P, _x̂, _P)                     # Track history
        
        return x̂, P, r, A
    

