#spline interpolation
#In 1D interpolation the points are fitted for a single curve whereas in Spline interpolation the points are fitted against a piecewise function defined with polynomials called splines.
#The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.
from scipy.interpolate import UnivariateSpline
import numpy

a=numpy.arange(10)
b=a**2 +numpy.sin(a) +1
c=UnivariateSpline(a,b)
d=c(numpy.arange(2.1,3,0.1))
print(d)
