#splitting arrays  ;'array_split()'
import numpy
a=numpy.array([1,2,3,4,5,6])
b=numpy.array_split(a,3)
print(b)

#if the the array has less elements than required it will adjust accordingly from the end
a=numpy.array([1,2,3,4,5,6])
b=numpy.array_split(a,4)
print(b)
#accessing the split arrays
print(b[0])
print(b[1])
print(b[2])
print(b[3])