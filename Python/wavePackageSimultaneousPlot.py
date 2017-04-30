#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
from scipy.integrate import quad

# Import the wave function and the function to calculate cn by Fourier's trick
from Psi import *
from getcn import *

x = np.linspace(0, 1, 2**11)
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

f = []

# Calculate the function for all times
for i in range(0, len(t)):
  f.append(Psi(cn, x, t[i]))

# Compute <x> and <x^2>

Ex = np.zeros(t.shape)
Ex2 = np.zeros(t.shape)

for i in range(0, len(t)):
  Ex[i] = np.trapz(x*(np.abs(f[i])**2), x = x)
  Ex2[i] = np.trapz(x**2*np.abs(f[i])**2, x = x)

STDx = np.sqrt(Ex2 - Ex**2)

# Compute <p> and <p^2>

Ep = np.zeros(t.shape, dtype = "complex128")
Ep2 = np.zeros(t.shape, dtype = "complex128")

dx = x[1] - x[0]
for i in range(0, len(t)):
  Ep[i] = np.trapz(np.conjugate(f[i])*(-1j)*np.gradient(f[i], dx), x = x)
  Ep2[i] = -np.trapz(np.conjugate(f[i])*np.gradient(np.gradient(f[i], dx), dx), x = x)
  
STDp = np.sqrt(Ep2 - Ep**2)

print("Uncertainty principle holds: " + str((STDx*STDp >= 0.5).all()))

# Calculate the momentum spectrum
p = np.linspace(-150, 150, 2**9)
pdist = []

for i in range(0, len(t)):
  if i % 2**8 == 0:
    print("%.2f" %(i/len(t)))
    
  tmp = np.zeros(p.shape, dtype=np.complex128)
  for j in range(0, len(p)):
    tmp[j] = np.trapz(np.conj(1/np.sqrt(2*np.pi)*np.exp(1j*p[j]*x))*f[i], x = x)
  
  pdist.append(tmp)

# Animate the wave using matplotlib

def animate(i):
  title.set_text("t = " + str(t[i]))

  # Wave package
  line1.set_data(x, np.abs(f[i]))
  annotation1.xy = (Ex[i], -1)
  annotation1.set_position((Ex[i], -0.7))
  
  # Momentum spectrum
  line2.set_data(p, np.abs(pdist[i])**2)
  
  # Uncertainty principle
  annotation3.xy = (t[i], (STDx*STDp)[i])
  annotation3.set_position((t[i], (STDx*STDp)[i] + 0.5))
  
  return line1, annotation1, line2, annotation3, title # We have to return all the objects we change
  
fig = plt.figure()
ax3 = fig.add_subplot(2, 1, 2) # The uncertainty principle
ax1 = fig.add_subplot(2, 2, 1) # The wave package
ax2 = fig.add_subplot(2, 2, 2) # The momentum spectrum


# Wave package
line1 = Line2D([], [])
ax1.add_line(line1)
ax1.set_title("Wave function")
ax1.set_xlabel("$x/a$")
ax1.set_xlim(0, 1)
ax1.set_ylim(-1, 3)
annotation1 = ax1.annotate(r"$\langle x \rangle$", xy = (Ex[0], -1), xytext = (Ex[0], -0.7), arrowprops = dict(facecolor = "black", shrink = 0.05), )

# Momentum spectrum
line2 = Line2D([], [])
ax2.set_title("Momentum spectrum")
ax2.add_line(line2)
ax2.set_xlabel("$p$")
ax2.set_xlim(p[0], p[-1])
ax2.set_ylim(0, 0.10)

# Uncertainty principle
line3, = ax3.semilogy(t, STDx*STDp)
ax3.set_title("Uncertainty principle")
ax3.set_xlabel("$t$")
ax3.set_xlim(0, t[-1])
annotation3 = ax3.annotate("", xy = (t[0], (STDx*STDp)[0]), xytext = (t[0], (STDx*STDp)[0] + 0.5), arrowprops = dict(facecolor = "black", shrink = 0.05), )

title = fig.suptitle("")

anim = animation.FuncAnimation(fig, animate, frames = len(t), interval = 20, blit = False)

#plt.show()

anim.save("wavePackageSimultaneousPlot.webm", writer="ffmpeg", fps = 30, codec="vp9", dpi=200)
