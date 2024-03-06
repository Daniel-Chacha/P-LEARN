#iterating arrays with different data types
#'op_dtypes' is used to change the datatype of elements while iterating
#'flags=['buffered']' is the extra space called buffer needed by numpy to change the datatype of the  elements in place
import numpy
a=numpy.array([1,2,3])

for x in numpy.nditer(a,flags=['buffered'],op_dtypes=['S']):
    print(x)


#iterating with different step sizes
b=numpy.array([[1,2,3,4],[6,7,8,9]])
for x in numpy.nditer(b[:, ::2]):
    print(x)

#also written as
for x in numpy.nditer(b[0:2, 0:5:2]):
    print(x)