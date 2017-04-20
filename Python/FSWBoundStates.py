import numpy as np
import matplotlib.pyplot as plt

z0 = 8

z = np.linspace(1, z0, 10**6)

h = np.tan(z) - np.sqrt(z0/z - 1)
dhdzA = 1/(np.cos(z))**2 + z0/(2*np.sqrt(z0/z-1)*z**2) # Analytical expression for the derivative
dz = z[1] - z[0]
dhdzN = np.gradient(h, dz) # Numerical calculation of the derivatve

plt.plot(z, dhdzA, label = "Analytic")
plt.plot(z, dhdzN, label = "Numerical")
plt.legend()
plt.show()
