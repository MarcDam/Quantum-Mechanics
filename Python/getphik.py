# Calculate cn by Fourier's trick

import numpy as np

# Import the stationary states
from FSW_psi_n_scattering import *

def getphik(x, f, E):

  k = np.sqrt(2*E)

  phik = np.zeros(k.shape, dtype = "complex128")

  for i in range(0, len(k)):
    phik[i] = np.trapz(np.conjugate(psi_k(E[i], x))*f, x = x)
      
  return phik
