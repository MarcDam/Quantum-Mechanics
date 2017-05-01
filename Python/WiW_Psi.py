import numpy as np

from WiW_Psi_n import *

def Psi(cn, x, t):
  try:
    output = np.zeros(x.shape, dtype = np.dtype("complex128"))
  except AttributeError:
    output = 0
    
  for i, ci in enumerate(cn):
    output += ci*Psi_n(i, x, t)
  
  return output
  
