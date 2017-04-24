import numpy as np

from FSW_Psi_n_bound import *

def Psi(cn, x, t):
  try:
    output = np.zeros(x.shape, dtype = np.dtype("complex128"))
  except AttributeError:
    output = 0
    
  for i, ci in enumerate(cn):
    output += ci*Psi_n(i, x, t)
  
  return output
  
