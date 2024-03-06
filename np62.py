#GCD
import numpy
a=6
b=9
c=numpy.gcd(a,b)
print(c)

#GCD of an array
d=numpy.array([20, 8, 32, 36, 16])
e=numpy.gcd.reduce(d)
print(e)