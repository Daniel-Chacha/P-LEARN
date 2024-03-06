#shape of an array refers to the number of elements in an array
import numpy
a=numpy.array([[1,2,3,4],[6,7,8,9]])
print(a.shape)

#create a 5-D array
b=numpy.array([1,2,3,4],ndmin=5)
print(b)
print(b.shape)