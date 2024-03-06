#create an array with data type 4 bytes integer
import numpy
m=numpy.array([1,2,3,4],dtype='i8')
print(m)
print(m.dtype)

#the best way to change the data type is to make a copy of the array using the 'astype()'
n=numpy.array([1.1,2.2,3.3,4.4])
o=n.astype('i')
print(o)
print(o.dtype)

#change datatype to boolean
p=numpy.array([1,0,3])
q=p.astype('bool')
print(q)
print(q.dtype)