#checking data type of numpy; use .'dtype'
import numpy
m=numpy.array([1,2,3,4])
print(m.dtype)

n=numpy.array(['apples','mangoes','guavas'])
print(n.dtype)

#creating array with defined data type
o=numpy.array([1,2,3,4],dtype='S')
print(o)
print(o.dtype)