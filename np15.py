#iterating using 'nditer()' function
import numpy
a=numpy.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in numpy.nditer(a):
    print(x)