#reshaping arrays
#change the 1-D  to 2-D
import numpy
m=numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
n=m.reshape(4,3)
print(n)

#1-D  to 3-D
m=numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
o=m.reshape(2,3,2)
print(o)

#check if the returned array is a copy or view
m=numpy.array([1,2,3,4,5,6,7,8])
print(m.reshape(2,4).base)