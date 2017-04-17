import numpy as np
from scipy.integrate import quad

#Import the stationary states
from ISW_psi_n import *

nMax = 10

integrals = np.zeros((nMax, nMax))

for i in range(1, nMax + 1):
  for j in range(1, nMax + 1):
    f = lambda x: np.conjugate(psi_n(i, x))*psi_n(j, x)
    integrals[i-1][j-1] = quad(f, 0, 1)[0]
    
print(integrals)
