import numpy as np

V0 = 13

def psi_k(E, x):
  # NB! k =< 0 not allowed
  k = np.sqrt(2*E)
  l = np.sqrt(2*(E+V0))
  F = np.exp(-2*1j*k)/(np.cos(2*l)-1j*(k**2+l**2)/(2*k*l)*np.sin(2*l))
  B = 1j*np.sin(2*l)/(2*k*l)*(l**2-k**2)*F
  C = (np.sin(l) + 1j*k/l*np.cos(l))*np.exp(1j*k)*F
  D = (np.cos(l) - 1j*k/l*np.sin(l))*np.exp(1j*k)*F
  psi = np.piecewise(x, [x > 1, 1 >= x, -1 > x], [lambda x: F*np.exp(1j*k*x), lambda x: C*np.sin(l*x) + D*np.cos(l*x), lambda x: np.exp(1j*k*x) + B*np.exp(-1j*k*x)]) # Not normalized
  A = np.trapz(np.abs(psi)**2, x = x) # Normalization constant
  
  return psi/A

