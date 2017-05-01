import numpy as np

from WiW_psi_n import *

def Psi_n(n, x, t):
  return psi_n(n, x)*np.exp(-1j*energy(n)*t)
