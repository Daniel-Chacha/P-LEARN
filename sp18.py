#Interpolation with Radial Basis Function
#Radial basis function is a function that is defined corresponding to a fixed reference point.
#The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.
#Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:

from scipy.interpolate import Rbf
import numpy

a=numpy.arange(10)
b=a**2 + numpy.sin(a) + 1
c=Rbf(a,b)
d=c(numpy.arange(2.1,3,0.1))
print(d)