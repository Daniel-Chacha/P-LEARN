#joining arrays  ; 'concatenate()'
import numpy 
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.concatenate((a,b))

print(c)

#join two 2D arrays along rows(axis=1)
d=numpy.array([[1,2],[3,4]])
e=numpy.array([[5,6],[7,8]])
f=numpy.concatenate((d,e),axis=1)

print(f)