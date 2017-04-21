#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from numpngw import AnimatedPNGWriter

# Import the wave function and the function to calculate cn by Fourier's trick
from Psi import *
from getcn import *

x = np.linspace(0, 1, 2**12)
t = np.linspace(0, 4/(np.pi), 2**13)

# Wave package constants
x0 = 0.5;
sigma = 0.1;
k0 = 100;

# Normalize the custom wave function and get the cn's
fun = np.exp(-1/2 * (x-x0)**2/sigma**2) * np.exp(-1j*k0*x)

A = 1/np.sqrt(np.trapz(np.abs(fun)**2, x = x))

fun = A * fun

cn = getcn(x, fun)

# Check normalization

f = lambda x: np.conjugate(Psi(cn, x, t[0]))*Psi(cn, x, t[0])
integral = quad(f, 0, 1)[0]

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

plt.plot(energy(np.arange(len(cn))), np.abs(cn)**2, 'ro')
plt.title("Energy spectrum")
plt.xlabel(r"$| c_n |^2$")
plt.ylabel(r"$E_n$")

plt.show()