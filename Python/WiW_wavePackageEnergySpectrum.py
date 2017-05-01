#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Import the wave function and the function to calculate cn by Fourier's trick
from WiW_Psi import *
from WiW_psi_n import energy
from WiW_getcn import *

x = np.linspace(-3, 3, 2**12)

# Wave package constants
x0 = 2.5;
sigma = 0.1;
k0 = 25;

# Normalize the custom wave function and get the cn's
fun = np.exp(-1/2 * (x-x0)**2/sigma**2) * np.exp(-1j*k0*x)

A = 1/np.sqrt(np.trapz(np.abs(fun)**2, x = x))

fun = A * fun

cn = getcn(x, fun)

# Check normalization

f = np.abs(Psi(cn, x, 0))**2
integral = np.trapz(f, x = x)

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

# Plot energy spectrum

energies = np.zeros(cn.shape)

for i in range(len(cn)):
  energies[i] = energy(i)

plt.plot(energies, np.abs(cn)**2, 'o')
plt.xlabel("Energy")
plt.ylabel("$|c_n|^2$")
plt.show()
