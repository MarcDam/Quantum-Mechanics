#!/usr/bin/python3

import ISW_psi_n as ISW
import FSW_psi_n_bound as FSW
import numpy as np

def psi_n(n, x):
  if n < len(FSW.energiesOrdered):
    return FSW.psi_n(n, x)
  else:
    return 1/np.sqrt(x[-1]-x[0])*ISW.psi_n(n - len(FSW.energiesOrdered) + 1, (x - x[0])/(x[-1]-x[0]))
    
def energy(n):
  if n < len(FSW.energiesOrdered):
    return FSW.energiesOrdered[n][0]
  else:
    return ISW.energy(n - len(FSW.energiesOrdered) + 1)
    
