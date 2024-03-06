#unknown dimension ; pass '-1' as the value
import numpy 
m=numpy.array([1,2,3,4,5,6,7,8])
n=m.reshape(2,2,-1)
print(n)

#flattening an array; converting multidimensional array into a 1D
#we use 'reshape(-1)'
r=numpy.array([[1,2,3],[4,5,6]])
s=r.reshape(-1)
print(s)
r=numpy.array([[1,2,3],[4,5,6]])
t=numpy.ravel(r)
print(t)