#finding the index where a values is   ;'where()' is used
import numpy
a=numpy.array([1,2,3,4,5,4,4])
b=numpy.where(a==4)
print(b)

#find index where values are even
c=numpy.array([1,2,3,4,5,6,7,8,9])
d=numpy.where(c%2==0)
print(d)

#index where value is odd
c=numpy.array([1,2,3,4,5,6,7,8,9])
d=numpy.where(c%2==1)
print(d)