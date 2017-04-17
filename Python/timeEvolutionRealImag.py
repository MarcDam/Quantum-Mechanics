#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpngw import AnimatedPNGWriter

# Import the time dependent states
from Psi_n import *

fig = plt.figure()
ax = plt.axes(xlim = (0, 1), ylim = (-2, 2))

lines = []
for i in range(0, 2):
  line, = plt.plot([], [], lw = 2)
  lines.append(line)

n = 3
  
x = np.linspace(0, 1, 256)
t = np.linspace(0, 4/(np.pi*n**2), 128)

def animate(i):
  y = Psi_n(n, x, t[i])
  lines[0].set_data(x, np.real(y))
  lines[1].set_data(x, np.imag(y))
  return lines
  
anim = animation.FuncAnimation(fig, animate, frames = 128, interval = 20, blit = True)

#plt.show()

writer = AnimatedPNGWriter(fps=30)

anim.save("timeEvolutionRealImag.png", dpi = 100, writer=writer)
