import numpy as np
import matplotlib.pyplot as plt

def hFunEven(z):
  return np.tan(z) - np.sqrt((z0/z)**2 - 1)
  
def hFunOdd(z):
  return -1/np.tan(z) - np.sqrt((z0/z)**2 - 1)
  
hfuns = [hFunEven, hFunOdd]
guesses = [(1, 0.5), (2, 1)]

z0 = np.sqrt(2*13)

z = np.linspace(1, z0, 10**6)

h = hFunEven(z)
dhdzA = 1/(np.cos(z))**2 + z0/(2*np.sqrt(z0/z-1)*z**2) # Analytical expression for the derivative
dz = z[1] - z[0]
dhdzN = np.gradient(h, dz) # Numerical calculation of the derivatve

plt.plot(z, dhdzA, label = "Analytic")
plt.plot(z, dhdzN, label = "Numerical")
plt.legend()
plt.show()

# Newton's root finding method

print("Newton's method:")

accuracy = 10**(-6)
guess = np.pi/2-0.1
roots = []

while guess < z0:
  zi = zinext = guess
  
  while abs(zi - zinext) < accuracy:
    zi = zinext
    zinext = zi - (hFunEven(zi))/(1/(np.cos(zi))**2 + z0/(2*np.sqrt(z0/zi-1)*zi**2))
    
  roots.append(zinext)
  guess = zinext + np.pi
    
  print(zinext)
  
# Bisection method

print("Bisection method:")
  
for i, hfun in enumerate(hfuns):
  print("i = " + str(i))
    
  guess = guesses[i][0]
  bisecRoots = []
    
  while guess < z0:
    a = guess - guesses[i][1]
    b = guess + guesses[i][1]
    if b > z0:
      b = z0 - 10**-2
    fa = hfun(a)
    fb = hfun(b)
    root = True
    
    print("Searching between %.2f and %.2f" %(a, b))
    
    while b - a > accuracy:
      fm = hfun((a + b)/2)
      
      if fa*fm < 0:
        b = (a + b)/2
        fb = fm
      elif fm*fb < 0:
        a = (a + b)/2
        fa = fm
      else:
        print("No root found in the interval from %.2f to %.2f" %(a, b))
        root = False
        break
    
    if root:
      print(a)
      bisecRoots.append(a)
    guess = a + 2*guesses[i][1]
    
