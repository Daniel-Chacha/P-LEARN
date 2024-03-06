#find index where a value should be inserted;  searchsorted() method is used
#it is assumed to be used on sorted arrays
import numpy
a=numpy.array([6,7,8,9])
b=numpy.searchsorted(a,7)
print(b)

#by default the leftmost index is returned, but we can give the side='right' to return the rightmost index
a=numpy.array([6,7,8,9])
b=numpy.searchsorted(a,7,side='right')
print(b)

#multiple values
c=numpy.array([1,3,5,7])
d=numpy.searchsorted(c,[2,4,6])
print(d)