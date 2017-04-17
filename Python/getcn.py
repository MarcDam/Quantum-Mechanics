# Calculate cn by Fourier's trick

import numpy as np

# Import the stationary states
from ISW_psi_n import psi_n

def getcn(x, f, epsilon = 10**(-12), n = 0):

  cn = np.array(0)

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
      
  if n == 0:
    print("Required " + str(len(cn)) + " cn's to get below " + str(epsilon) + " error")
      
  return cn
