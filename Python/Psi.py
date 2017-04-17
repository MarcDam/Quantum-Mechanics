import numpy as np

# Import the time dependent states 
from Psi_n import *

def Psi(cn, x, t):
  try:
    output = np.zeros(x.shape, dtype = np.dtype("complex128"))
  except AttributeError:
    output = 0
    
  for i, ci in enumerate(cn, 1):
    output += ci*Psi_n(i, x, t)
  
  return output
  
