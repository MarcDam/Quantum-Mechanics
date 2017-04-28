import numpy as np

from FSW_psi_n_scattering import *

def Psi(phik, E, x, t):
  try:
    output = np.zeros(x.shape, dtype = np.dtype("complex128"))
  except AttributeError:
    output = 0
    
  k = np.sqrt(2*E)
    
  integrand = np.zeros((len(E), len(x)), dtype = "complex128")
  
  for i in range(0, len(E)):
    integrand[i] = phik[i]*psi_k(E[i], x)*np.exp(-1j*E[i]*t)
  
  output = np.trapz(integrand, x = k, axis = 0)
  
  return output
  
