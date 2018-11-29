from numpy import *
import matplotlib.pyplot as plt
import math

def f(x):
    return -x**cos(5*x)

x=linspace(1,10,250)

plt.plot(x,f(x),label='-x^cos(5*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('zavd14.png',dpi=200)
plt.show()
