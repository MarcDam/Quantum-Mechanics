import numpy as np

# Import the stationary states and their energies
from ISW_psi_n import *

def Psi_n(n, x, t):
  return psi_n(n, x)*np.exp(-1j*energy(n)*t)

