import numpy as np
import matplotlib.pyplot as plt

def psi_n(n, x):
  E = energy(n)
  
  if E[1] == "even":
    i = energies["even"].index(E[0])

    return psi_n_even(i, x)
    
  else:
    i = energies["odd"].index(E[0])
    
    return psi_n_odd(i, x)

def psi_n_even(n, x):
  k = np.sqrt(2*energies["even"][n])
  l = np.sqrt(2*(energies["even"][n] + V0))
  A = 1/np.sqrt(-(1-b) + np.sin(2*k*(1-b))/(2*k) + (np.sin(k*(1-b))/np.cos(l))**2*(1 + np.sin(2*l)/(2*l)))
  D = A * np.sin(k*(1-b))/np.cos(l)
  return np.piecewise(x, [x > b, np.logical_and(x <= b, x >= 1), np.logical_and(x <= 1, x >= -1), np.logical_and(x <= -1, x >= -b), x < -b], [0, lambda x: A*np.sin(k*(x-b)), lambda x: D*np.cos(l*x), lambda x: A*np.sin(k*(-x - b)), 0])

def psi_n_odd(n, x):
  k = np.sqrt(2*energies["odd"][n])
  l = np.sqrt(2*(energies["odd"][n] + V0))
  A = 1/np.sqrt(-(1-b) + np.sin(2*k*(1-b))/(2*k) + (np.sin(k*(1-b))/np.sin(l))**2*(1 - np.sin(2*l)/(2*l)))
  D = A * np.sin(k*(1-b))/np.sin(l)
  return np.piecewise(x, [x > b, np.logical_and(x <= b, x >= 1), np.logical_and(x <= 1, x >= -1), np.logical_and(x <= -1, x >= -b), x < -b], [0, lambda x: A*np.sin(k*(x-b)), lambda x: D*np.sin(l*x), lambda x: -A*np.sin(k*(-x - b)), 0])
  
def energy(n):
  if len(energiesOrdered) <= n:
    findEnergies(n)

  return energiesOrdered[n][0]
  
def hFunEven(z):
  return z*np.tan(z)*np.tan(np.sqrt(z**2 - z0**2) * (1 - b)) + np.sqrt(z**2 - z0**2)
  
def hFunOdd(z):
  return z*(1/np.tan(z))*np.tan(np.sqrt(z**2 - z0**2) * (1 - b)) - np.sqrt(z**2 - z0**2)
  
def dhdzFunEven(z):
  s = np.sqrt(z**2 - z0**2)
  
  return np.tan(z)*np.tan(s*(1-b)) + z * ((1/(np.cos(z))**2)*np.tan(s*(1-b)) + (1-b)*z*np.tan(z)*(1/(s*np.cos(s*(1-b))**2))) + z/s
 
def dhdzFunOdd(z):
  s = np.sqrt(z**2 - z0**2)

  return (1/np.tan(z))*np.tan(s*(1-b)) + z * ((-1/(np.sin(z))**2)*np.tan(s*(1-b)) + (1-b)*z*(1/np.tan(z))*(1/(s*np.cos(s*(1-b))**2))) - z/s
  
V0 = 13
b = 3

z0 = np.sqrt(2*V0)
  
hfuns = [hFunEven, hFunOdd]
dhdzfuns = [dhdzFunEven, dhdzFunOdd]

energies = {}
energies["even"] = []
energies["odd"] = []
energiesOrdered = []

def findEnergies(n):
  print("Newton's method:")
  niter = 10**4
  
  if len(energies["even"]) > 0 and len(energies["odd"]) > 0:
    guesses = [[np.sqrt(2*(energies["even"][-1] + V0)) + 0.9, 0.9, 1], [np.sqrt(2*(energies["odd"][-1] + V0)) + 0.9, 0.9, 1]]
  else:
    guesses = [[z0 + 0.2, 0.9, 1], [z0 + 0.1, 0.9, 1]]
  
  while len(energiesOrdered) < n:
    for i, hfun in enumerate(hfuns):
      dhdz = dhdzfuns[i]
      zi = guesses[i][0]
      
      for j in range(niter):
        zi = zi - hfun(zi)/dhdz(zi)
      
      print(hfun)
      print(zi)
      
      E = zi**2/2 - V0
      
      index = 0
      for Eo in energiesOrdered:
        if E > Eo[0]:
          index += 1
        else:
          break
      
      if i == 0:
        energies["even"].append(E)
        energiesOrdered.insert(index, (E, "even"))
      else:
        energies["odd"].append(E)
        energiesOrdered.insert(index, (E, "odd"))
        
      # Good guesses are hard so we tweak our guesses a little as we go
      if i == 0 and len(energies["even"]) == 1:
        guesses[i][0] = zi + 0.5
      elif i == 0 and len(energies["even"]) == 2:
        guesses[i][0] = zi + 1.3
      elif i == 1 and len(energies["odd"]) == 1:
        guesses[i][0] = zi + 0.6
      elif len(energies[["even", "odd"][i]]) <= 10:
        guesses[i][0] = zi + guesses[i][1]
      else:
        guesses[i][0] = zi + guesses[i][2]

# Plot the bound states

#findEnergies(8)

#x = np.linspace(-b, b, 200*b)
#    
#for i in range(0, len(energies["even"])):
#  plt.plot(x, energies["even"][i] + psi_n_even(i, x), label = "Even, energy: " + str(energies["even"][i] ))
#  
#for i in range(0, len(energies["odd"])):
#  plt.plot(x, energies["odd"][i] + psi_n_odd(i, x), label = "Odd, energy: " + str(energies["odd"][i] ))
#  
#plt.plot(x, np.piecewise(x, [x > 1, np.logical_and(1 >= x, x >= -1), -1 > x], [0, -V0, 0]))
##plt.ylim(-V0-1, 1)
#plt.xlabel("$x/a$")
#plt.ylabel("$\psi(x)$")
##plt.legend()
#plt.show()
##plt.savefig("WiW_negative.png")
