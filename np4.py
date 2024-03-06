#creating an array with 5-D and verifying
import numpy

x=numpy.array([1,2,3,4],ndmin=5)
print(x)
print('This is a ',x.ndim ,' dimension array')