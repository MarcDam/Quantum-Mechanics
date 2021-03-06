#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Import the wave function
from FSW_Psi_bound import *

cn = 1/np.sqrt(3)*np.array([1, 1, 1, 1])
  
x = np.linspace(-2, 2, 256)
t = np.linspace(0, 10, 2**11)

# Check normalization

f = np.abs(Psi(cn, x, t[0]))**2
integral = np.trapz(f, x = x)

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

# Calculate the function for all times
f = []

for i in range(0, len(t)):
  f.append(Psi(cn, x, t[i]))

for i, fi in enumerate(f):
  if (np.abs(fi - f[0]) < 10**-8).all():
    print(i)

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

print("Uncertainty principle holds: " + str((STDx*STDp > 0.5).all()))

def animate(i):
  line.set_data(x, np.abs(f[i]))
  annotation.xy = (Ex[i], -1)
  annotation.set_position((Ex[i], -0.7))
  return line, annotation
  
fig = plt.figure()
ax = plt.axes(xlim = (x[0], x[-1]), ylim = (-1, 2))

line, = plt.plot([], [], lw = 2)

annotation = ax.annotate(r"$\langle x \rangle$", xy = (Ex[0], -1), xytext = (Ex[0], -0.7), arrowprops = dict(facecolor = "black", shrink = 0.05), )

anim = animation.FuncAnimation(fig, animate, frames = len(t), interval = 20, blit = True)

plt.show()

#writer = AnimatedPNGWriter(fps=30)

#anim.save("nonStationaryModulus.png", dpi = 100, writer=writer)
