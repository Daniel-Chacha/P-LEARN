#product
import numpy
a=numpy.array([1,2,3,4])
b=numpy.prod(a)
print(b)

#product of two elements of an array
c=numpy.array([1,2,3,4])
d=numpy.array([5,6,7,8])
e=numpy.prod([c,d])
print(e)

#product over an axis
f=numpy.array([1,2,3,4])
g=numpy.array([5,6,7,8])
h=numpy.prod([f,g],axis=1)
print(h)

#cummulative product ;taking the product partially.
#E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
i=numpy.array([5,6,7,8])
j=numpy.cumprod(i)
print(j)