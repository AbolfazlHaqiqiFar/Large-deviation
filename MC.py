import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
import sympy as smp

x = np.linspace(0, 3, 100)
f = 2*np.exp(-2*x)
F = 1- np.exp(-2*x)

plt.figure(1, figsize=(8, 3))
plt.plot(x, f, label= r'$f(x)$')
plt.plot(x, F, label= r'$F(x)$')
plt.legend()
plt.xlabel(r'$x$', fontsize = 10)
plt.close(1)


Us = np.random.rand(10000)
F_inv_Us = -np.log(1-Us)/2

plt.figure(2, figsize=(8, 3))
plt.plot(x, f , label= r'$f(x)$')
plt.hist(F_inv_Us,density='norm', bins=100)
plt.legend()
plt.show()


