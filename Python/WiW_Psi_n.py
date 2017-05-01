import numpy as np

from WiW_psi_n import *

def Psi_n(n, x, t):
  if n < len(FSW.energiesOrdered):
    E = FSW.energiesOrdered[n][0]
  else:
    E = ISW.energy(n - len(FSW.energiesOrdered) + 1)
  
  return psi_n(n, x)*np.exp(-1j*E*t)
