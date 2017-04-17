#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from numpngw import AnimatedPNGWriter

# Import the wave function and the function to calculate cn by Fourier's trick
from Psi import *
from getcn import *

x = np.linspace(0, 1, 256)
t = np.linspace(0, 4/(np.pi), 256)

# Normalize the custom wave function and get the cn's
fun = x**3 * (1 - x)

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

# Compute <x> and <x^2>

Ex = np.zeros(t.shape)
Ex2 = np.zeros(t.shape)

for i in range(0, len(t)):
  Ex[i] = np.trapz(x*(np.abs(Psi(cn, x, t[i]))**2), x = x)
  Ex2[i] = np.trapz(x**2*np.abs(Psi(cn, x, t[i]))**2, x = x)

STDx = np.sqrt(Ex2 - Ex**2)

# Compute <p> and <p^2>

Ep = np.zeros(t.shape)
Ep2 = np.zeros(t.shape)

dx = x[1] - x[0]
for i in range(0, len(t)):
  Ep[i] = np.trapz(np.conjugate(Psi(cn, x, t[i]))*(-1j)*np.gradient(Psi(cn, x, t[i]), dx), x = x)
  Ep2[i] = -np.trapz(np.conjugate(Psi(cn, x, t[i]))*np.gradient(np.gradient(Psi(cn, x, t[i]), dx), dx), x = x)
  
STDp = np.sqrt(Ep2 - Ep**2)

print("Uncertainty principle holds: " + str((STDx*STDp > 0.5).all()))

# Animate the wave using matplotlib

def animate(i):
  line.set_data(x, np.abs(Psi(cn, x, t[i])))
  annotation.xy = (Ex[i], -1)
  annotation.set_position((Ex[i], -0.7))
  return line, annotation # We have to return all the objects we change
  
fig = plt.figure()
ax = plt.axes(xlim = (0, 1), ylim = (-1, 2))

line, = plt.plot([], [], lw = 2)

annotation = ax.annotate(r"$\langle x \rangle$", xy = (Ex[0], -1), xytext = (Ex[0], -0.7), arrowprops = dict(facecolor = "black", shrink = 0.05), )

anim = animation.FuncAnimation(fig, animate, frames = 256, interval = 20, blit = True)

#plt.show()

# Use numpngw to make an animated png from the matplotlib animation
writer = AnimatedPNGWriter(fps=30)

anim.save("customWave.png", dpi = 100, writer=writer)
