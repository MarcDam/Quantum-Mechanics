#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from WiW_psi_n import *

n = 8

pos.findEnergies(n)

# Plot some of the stationary states

V0 = pos.V0
b = pos.b

x = np.linspace(-b, b, 200*b)
    
for i in range(0, n):
  plt.plot(x, energy(i) + psi_n(i, x), label = "E: " + str(energy(i)))
  
xW = np.linspace(-b - 0.1, b + 0.1, 200*b)
    
plt.plot(xW, np.piecewise(xW, [xW > b, np.logical_and(xW <= b, xW > 1), np.logical_and(1 >= xW, xW >= -1), np.logical_and(-1 > xW, xW >= -b), -b > xW], [10 + energy(n), 0, -V0, 0, 10 + energy(n)]))
plt.ylim(-V0-1, energy(n - 1) + 1)
plt.xlabel("$x/a$")
plt.ylabel("$\psi(x)$")
#plt.legend()
#plt.show()
plt.savefig("WiW_stationarySolutions.png")
