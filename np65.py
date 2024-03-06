#hyperbolic functions
#NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
import numpy
a=numpy.sinh(numpy.pi/2)
print(a)

print('\n')
#cosh values
b=numpy.cosh([numpy.pi/2,numpy.pi/3,numpy.pi/4,numpy.pi/5])
c=numpy.cosh(b)
print(c)

print('\n')
#finding angles
#Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
#Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.
#finding the angle of 1.0
d=numpy.arcsinh(1.0)
print(d)

print('\n')
e=numpy.arctanh([0.1,0.2,0.5])
print(e)