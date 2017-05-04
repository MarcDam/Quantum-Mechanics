#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
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

f = np.abs(Psi(cn, x, t[0]))**2
integral = np.trapz(f, x = x)

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

f = []

# Calculate the function for all times
for i in range(0, len(t)):
  f.append(Psi(cn, x, t[i]))

print("Done calculating... Starting animation...")

# Animate the wave using matplotlib

def animate(i):
  line.set_data(x, np.real(f[i]))
  line.set_3d_properties(np.imag(f[i]))
  title.set_text("t = " + str(t[i]))
  return line, title # We have to return all the objects we change
  
fig = plt.figure()
ax = p3.Axes3D(fig, xlim = (0, 1), ylim = (-3, 3), zlim = (-3, 3))
ax.set_xlabel("x")
ax.set_ylabel("Re")
ax.set_zlabel("Im")

line, = ax.plot(x, np.real(f[0]), np.imag(f[0]), lw = 2)

title = plt.title("")

anim = animation.FuncAnimation(fig, animate, frames = len(t), interval = 20, blit = True)

plt.show()

anim.save("wavePackage3d.mp4", writer="ffmpeg", fps = 30, codec="h264")

### MEMORY ISSUES ###
# Use numpngw to make an animated png from the matplotlib animation
#writer = AnimatedPNGWriter(fps=30)

#anim.save("wavePackage.png", dpi = 100, writer=writer)
