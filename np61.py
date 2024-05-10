#LCM
import numpy
a=4
b=6
c=numpy.lcm(a,b)
print(c)

#finding lcm of an array
d=numpy.array([3,6,9])
e=numpy.lcm.reduce(d)
print(e)

#Find the LCM of all values of an array where the array contains all integers from 1 to 10:
f=numpy.arange(1,11)
#print(f)
g=numpy.lcm.reduce(f)
print(g)