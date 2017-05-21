#!/usr/bin/python3

import WiW_psi_n_positive as pos
import WiW_psi_n_negative as neg
import numpy as np

def psi_n(n, x):
  if n < len(neg.energiesOrdered):
    return neg.psi_n(n, x)
  else:
    return pos.psi_n(n - len(neg.energiesOrdered))
    
def energy(n):
  if n < len(neg.energiesOrdered):
    return neg.energy(n)
  else:
    return pos.energy(n - len(neg.energiesOrdered))
    
