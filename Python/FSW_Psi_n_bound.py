import numpy as np

from FSW_psi_n_bound import *

def Psi_n(n, x, t):
  E = energiesOrdered[n]
  
  if E[1] == "even":
    i = energies["even"].index(E[0])

    return psi_n_even(i, x)*np.exp(-1j*E[0]*t)
    
  else:
    i = energies["odd"].index(E[0])
    
    return psi_n_odd(i, x)*np.exp(-1j*E[0]*t)
