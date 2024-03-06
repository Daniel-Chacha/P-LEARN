#finding root of an equation
#This function takes two required arguments:
#fun - a function representing an equation.
#x0 - an initial guess for the root.
#find root of eqn x+cos(x)

from scipy.optimize import root
from math import cos

def eqn(x):
    return x+cos(x)

y=root(eqn,0)
print(y.x)
#print all info about the solution
print(y)