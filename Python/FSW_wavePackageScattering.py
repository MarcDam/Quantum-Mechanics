#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpngw import AnimatedPNGWriter

from getphik import *
from FSW_Psi_scattering import *

x = np.linspace(-30, 30, 2**8)
t = np.linspace(0, 0.001, 2**4)

# Wave package constants
x0 = 10;
sigma = 0.1;
k0 = 100;

# Normalize the custom wave function and get the cn's
fun = np.exp(-1/2 * (x-x0)**2/sigma**2) * np.exp(-1j*k0*x)

A = 1/np.sqrt(np.trapz(np.abs(fun)**2, x = x))

fun = A * fun

E = np.linspace(0.1, 10**5, 10**4)

phik = getphik(x, fun, E)

# Check normalization

f = np.abs(Psi(phik, E, x, t[0]))**2
integral = np.trapz(f, x = x)

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

f = []

# Calculate the function for all times
for i in range(0, len(t)):
  f.append(Psi(phik, E, x, t[i])/integral)

# Compute <x> and <x^2>

Ex = np.zeros(t.shape)
Ex2 = np.zeros(t.shape)

for i in range(0, len(t)):
  Ex[i] = np.trapz(x*(np.abs(f[i])**2), x = x)
  Ex2[i] = np.trapz(x**2*np.abs(f[i])**2, x = x)

STDx = np.sqrt(Ex2 - Ex**2)

# Compute <p> and <p^2>

Ep = np.zeros(t.shape)
Ep2 = np.zeros(t.shape)

dx = x[1] - x[0]
for i in range(0, len(t)):
  Ep[i] = np.trapz(np.conjugate(f[i])*(-1j)*np.gradient(f[i], dx), x = x)
  Ep2[i] = -np.trapz(np.conjugate(f[i])*np.gradient(np.gradient(f[i], dx), dx), x = x)
  
STDp = np.sqrt(Ep2 - Ep**2)

print("Uncertainty principle holds: " + str((STDx*STDp >= 0.5).all()))

# Animate the wave using matplotlib

def animate(i):
  line.set_data(x, np.abs(f[i]))
  annotation.xy = (Ex[i], -1)
  annotation.set_position((Ex[i], -0.7))
  title.set_text("t = " + str(t[i]))
  return line, annotation, title # We have to return all the objects we change
  
fig = plt.figure()
ax = plt.axes(xlim = (x[0], x[-1]), ylim = (-1, 3))

line, = plt.plot([], [], lw = 2)

annotation = ax.annotate(r"$\langle x \rangle$", xy = (Ex[0], -1), xytext = (Ex[0], -0.7), arrowprops = dict(facecolor = "black", shrink = 0.05), )

title = plt.title("")

anim = animation.FuncAnimation(fig, animate, frames = len(t), interval = 20, blit = True)

plt.show()

#anim.save("FSW_wavePackageScattering.webm", writer="ffmpeg", fps = 30, codec="vp9")

### MEMORY ISSUES ###
# Use numpngw to make an animated png from the matplotlib animation
#writer = AnimatedPNGWriter(fps=30)

#anim.save("wavePackage.png", dpi = 100, writer=writer)
