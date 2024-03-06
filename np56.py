#rounding off numbers
import numpy
a=numpy.trunc([-3.143,6.745])
print(a)
b=numpy.fix([-3.143,6.745])
print(b)

#round off to specific dp. 'around()
c=numpy.around([3.21653,8.4252],2)
print(c)

#floor the elements ;The floor() function rounds off decimal to nearest lower integer.
d=numpy.floor([2.543,7.89,5.64])
print(d)

#ceil ;The ceil() function rounds off decimal to nearest upper integer.
e=numpy.ceil([2.543,7.89,5.64])
print(e)