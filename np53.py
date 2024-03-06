#adding two elements without ufunc fucntion
x=[1,2,3,4]
y=[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

import numpy
x=[1,2,3,4]
y=[5,6,7,8]
b=numpy.add(x,y)
print(b)