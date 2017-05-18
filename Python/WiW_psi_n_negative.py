import numpy as np
import matplotlib.pyplot as plt

def psi_n(n, x):
  E = energiesOrdered[n]
  
  if E[1] == "even":
    i = energies["even"].index(E[0])

    return psi_n_even(i, x)
    
  else:
    i = energies["odd"].index(E[0])
    
    return psi_n_odd(i, x)

def psi_n_even(n, x):
  k = np.sqrt(-2*energies["even"][n])
  l = np.sqrt(2*(energies["even"][n] + V0))
  A = 1/np.sqrt((1-b) - np.sinh(2*k*(1-b))/(2*k) + (np.sinh(k*(1-b))/np.cos(l))**2*(1 + np.sin(2*l)/(2*l)))
  D = A * np.sinh(k*(1-b))/np.cos(l)
  return np.piecewise(x, [x > b, np.logical_and(x <= b, x >= 1), np.logical_and(x <= 1, x >= -1), np.logical_and(x <= -1, x >= -b), x < -b], [0, lambda x: A*np.sinh(k*(x-b)), lambda x: D*np.cos(l*x), lambda x: A*np.sinh(k*(-x - b)), 0])

def psi_n_odd(n, x):
  k = np.sqrt(-2*energies["odd"][n])
  l = np.sqrt(2*(energies["odd"][n] + V0))
  A = 1/np.sqrt((1-b) - np.sinh(2*k*(1-b))/(2*k) + (np.sinh(k*(1-b))/np.sin(l))**2*(1 - np.sin(2*l)/(2*l)))
  D = A * np.sinh(k*(1-b))/np.sin(l)
  return np.piecewise(x, [x > b, np.logical_and(x <= b, x >= 1), np.logical_and(x <= 1, x >= -1), np.logical_and(x <= -1, x >= -b), x < -b], [0, lambda x: A*np.sinh(k*(x-b)), lambda x: D*np.sin(l*x), lambda x: -A*np.sinh(k*(-x - b)), 0])
  
def energy(n):
  return energiesOrdered[n]
  
def hFunEven(z):
  return z*np.tan(z)*np.tanh(np.sqrt(z0**2 - z**2) * (1 - b)) + np.sqrt(z0**2 - z**2)
  
def hFunOdd(z):
  return z*(1/np.tan(z))*np.tanh(np.sqrt(z0**2 - z**2) * (1 - b)) - np.sqrt(z0**2 - z**2)
  
def dhdzFunEven(z):
  s = np.sqrt(z0**2 - z**2)
  
  return np.tan(z)*np.tanh(s*(1-b)) + z * (1/(np.cos(z))**2)*np.tanh(s*(1-b)) - (1-b)*z*np.tan(z)*(1/(s*np.cosh(s*(1-b))**2)) - z/s
 
def dhdzFunOdd(z):
  s = np.sqrt(z0**2 - z**2)

  return (1/np.tan(z))*np.tanh(s*(1-b)) + z * (-1/(np.sin(z))**2)*np.tanh(s*(1-b)) - (1-b)*z*(1/np.tan(z))*(1/(s*np.cosh(s*(1-b))**2)) + z/s
  
V0 = 13
b = 3

z0 = np.sqrt(2*V0)
  
hfuns = [hFunEven, hFunOdd]
dhdzfuns = [dhdzFunEven, dhdzFunOdd]
  
print("Newton's method:")

niter = 10**4
guesses = [(np.pi/2 - 0.1, np.pi), (np.pi-0.1, 2)]
newtonRoots = []

for i, hfun in enumerate(hfuns):
  print(str(hfun))
    
  guess = guesses[i][0]
  newtonRoots.append([])
  dhdz = dhdzfuns[i]

  while guess < z0:
    zi = guess
    
    for j in range(niter):
      zi = zi - hfun(zi)/dhdz(zi)
      
    newtonRoots[i].append(zi)
    guess = zi + guesses[i][1]
      
    print(zi)
    
# Calculate the energies and separate them into odd and even
    
energies = {}
energies["even"] = []
energies["odd"] = []
    
for i in range(0, len(newtonRoots[0])):
  energies["even"].append(newtonRoots[0][i]**2/2 - V0)
  
for i in range(0, len(newtonRoots[1])):
  energies["odd"].append(newtonRoots[1][i]**2/2 - V0)
  
# Order the energies (lowest first)
  
energiesOrdered = []

for key in energies:
  for i in energies[key]:
    index = 0
    for energy in energiesOrdered:
      if i > energy[0]:
        index += 1
      else:
        break
        
    energiesOrdered.insert(index, (i, key))

# Plot the bound states

#x = np.linspace(-b, b, 200*b)
#    
#for i in range(0, len(energies["even"])):
#  plt.plot(x, energies["even"][i] + psi_n_even(i, x), label = "Even, energy: " + str(energies["even"][i] ))
#  
#for i in range(0, len(energies["odd"])):
#  plt.plot(x, energies["odd"][i] + psi_n_odd(i, x), label = "Odd, energy: " + str(energies["odd"][i] ))
#  
#plt.plot(x, np.piecewise(x, [x > 1, np.logical_and(1 >= x, x >= -1), -1 > x], [0, -V0, 0]))
#plt.ylim(-V0-1, 1)
#plt.xlabel("$x/a$")
#plt.ylabel("$\psi(x)$")
##plt.legend()
#plt.show()
##plt.savefig("WiW_negative.png")
