#num set operations
#Convert following array with repeated elements to a set:
import numpy
a=numpy.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b=numpy.unique(a)
print(b)

#unique values of two arrays
c=numpy.array([1,2,3,4])
d=numpy.array([3,4,5,6])
e=numpy.union1d(c,d)
print(e)

#intersection of elements
f=numpy.array([1,2,3,4])
g=numpy.array([3,4,5,6])
h=numpy.intersect1d(f,g,assume_unique=True) #assume_unique is used to speed up cumputation
print(h)

#set difference
f=numpy.array([1,2,3,4])
g=numpy.array([3,4,5,6])
i=numpy.setdiff1d(f,g,assume_unique=True)
print(i)

#symetric difference
#To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
f=numpy.array([1,2,3,4])
g=numpy.array([3,4,5,6])
j=numpy.setxor1d(f,g,assume_unique=True)
print(j)