#Interpolation is a method for generating points between given points. 'scipy.interpolate '
#This method of filling values is called imputation.
#1D Interpolation
#The function interp1d() is used to interpolate a distribution with 1 variable.
#It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
#For given xs and ys interpolate values from 2.1, 2.2... to 2.9
from scipy.interpolate import interp1d
import numpy

a=numpy.arange(10)
b=2*a +1

c=interp1d(a,b)
d=c(numpy.arange(2.1,3,0.1))
print(d)