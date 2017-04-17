#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from numpngw import AnimatedPNGWriter

# Import the wave function
from Psi import *

cn = 1/np.sqrt(2)*np.array([1, 1])
  
x = np.linspace(0, 1, 256)
t = np.linspace(0, 4/(np.pi), 256)

f = lambda x: np.conjugate(Psi(cn, x, t[0]))*Psi(cn, x, t[0])
integral = quad(f, 0, 1)[0]

if integral == 1:
  print("Wave function is normalized")
else:
  print("Wave function is not normalized. Integral is " + str(integral))

Ex = np.zeros(t.shape)
Ex2 = np.zeros(t.shape)

for i in range(0, len(t)):
  Ex[i] = np.trapz(x*(np.abs(Psi(cn, x, t[i]))**2), x = x)
  Ex2[i] = np.trapz(x**2*np.abs(Psi(cn, x, t[i]))**2, x = x)

STDx = np.sqrt(Ex2 - Ex**2)

def animate(i):
  line.set_data(x, np.abs(Psi(cn, x, t[i])))
  annotation1 = ax.annotate(r"$\langle x \rangle$", xy = (Ex[i], -1), xytext = (Ex[i], -0.7), arrowprops = dict(facecolor = "black", shrink = 0.05), )
  return line, annotation1
  
fig = plt.figure()
ax = plt.axes(xlim = (0, 1), ylim = (-1, 2))

line, = plt.plot([], [], lw = 2)
  
anim = animation.FuncAnimation(fig, animate, frames = 256, interval = 20, blit = True)

#plt.show()

writer = AnimatedPNGWriter(fps=30)

anim.save("nonStationaryModulus.png", dpi = 100, writer=writer)
