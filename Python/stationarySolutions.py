#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Import the stationary states
from ISW_psi_n import *

nMax = 4

x = np.linspace(0, 1, num=100)

for i in range(1, nMax+1):
  plt.plot(x, psi_n(i, x), label="$n = " + str(i) + "$")
  
plt.legend()
plt.xlabel("$x/a$")
plt.ylabel("$\psi_n(x)$")
#plt.show()
plt.savefig("ISW_stationarySolutions.png")
