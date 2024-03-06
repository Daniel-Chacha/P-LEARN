#trigonometry
import numpy
#sin value of pi/2
s=numpy.sin(numpy.pi/2)
print(s)

print('\n')
#conversion to radians
a=numpy.deg2rad([90, 180, 270, 360])
print(a)

print('\n')
b=numpy.rad2deg([1.57,3.14,4.71,6.2])
print(b)

print('\n')
#finding angles from the values of sin,cos,tan
#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
c=numpy.arcsin(1.0)
print(c)