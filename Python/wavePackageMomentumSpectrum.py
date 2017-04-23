#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from numpngw import AnimatedPNGWriter

# Import the wave function and the function to calculate cn by Fourier's trick
from Psi import *
from getcn import *

x = np.linspace(0, 1, 2**10)
t = np.linspace(0, 4/(np.pi), 2**13)

# Wave package constants
x0 = 0.5
sigma = 0.1
k0 = 100

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

f = []

# Calculate the function for all times
for i in range(0, len(t)):
  f.append(Psi(cn, x, t[i]))

# Calculate the momentum spectrum
p = np.linspace(-200, 200, 2**10)
pdist = []

for i in range(0, len(t)):
  if i % 2**8 == 0:
    print("%.2f" %(i/len(t)))
    
  tmp = np.zeros(p.shape, dtype=np.complex128)
  for j in range(0, len(p)):
    tmp[j] = np.trapz(np.conj(1/np.sqrt(2*np.pi)*np.exp(1j*p[j]*x))*f[i], x = x)
  
  pdist.append(tmp)


# Animate the momentum distribution using matplotlib

def animate(i):
  line.set_data(p, np.abs(pdist[i])**2)
  title.set_text("t = " + str(t[i]))
  return line, title # We have to return all the objects we change
  
fig = plt.figure()
ax = plt.axes(xlim = (p[0], p[-1]), ylim = (0, 0.15))

line, = plt.plot([], [], lw = 2)

title = plt.title("")

anim = animation.FuncAnimation(fig, animate, frames = len(t), interval = 20, blit = True)

plt.show()

anim.save("wavePackageMomentumSpectrum.webm", writer="ffmpeg", fps = 30, codec="vp9")

### MEMORY ISSUES ###
# Use numpngw to make an animated png from the matplotlib animation
#writer = AnimatedPNGWriter(fps=30)

#anim.save("wavePackage.png", dpi = 100, writer=writer)
