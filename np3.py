#checking the number of arrays
import numpy

x=numpy.array(42)
y=numpy.array([1,2,3,4])
z=numpy.array([[1,2,3,4],[6,7,8,9]])
n=numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[4,3,2]]])

print(x.ndim)
print(y.ndim)
print(z.ndim)
print(n.ndim)