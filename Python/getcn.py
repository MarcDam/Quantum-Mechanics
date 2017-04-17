# Calculate cn by Fourier's trick

import numpy as np

# Import the stationary states
from ISW_psi_n import psi_n

def getcn(x, f, epsilon = 10**(-6), n = 0):

  cn = np.array()

  if n == 0:
    i = 1
    
    while np.sqrt(cn.dot(cn)) < 1 - epsilon:
      cn = np.append(cn, np.trapz(np.conjugate(psi_n(i, x))*f, x = x))
      i += 1
    
  else:
    i = 1
    
    while i <= len(cn):
      cn = np.append(cn, np.trapz(np.conjugate(psi_n(i, x))*f, x = x))
      i += 1
      
  return cn
