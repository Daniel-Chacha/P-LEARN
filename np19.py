#joining arrays using using stack functions
#stacking joins along a new axis
import numpy 
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.stack((a,b),axis=1)

print(c,'\n')

#stacking along rows
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.hstack((a,b))

print(c,'\n')

#stacking along columns
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.vstack((a,b))

print(c,'\n')

#stacking along a height (depth)  ;'dstack()
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.dstack((a,b))

print(c)
