import numpy as np

def psi_n(n, x):
  return np.sqrt(2)*np.sin(n*np.pi*x)
  
def energy(n):
  return (n**2*np.pi**2)/2
