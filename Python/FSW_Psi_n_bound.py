import numpy as np

from FSW_psi_n_bound import *

def Psi_n(n, x, t):
  E = energiesOrdered[n]
  
  return psi_n(n, x)*np.exp(-1j*E[0]*t)
