#accessing arrays
import numpy
x=numpy.array([1,2,3,4])
print(x[1])

#get third and fourth element and add them
print(x[2]+x[3])

#accessing 2-D arrays;item on 1st row ,2nd column
y=numpy.array([[1,2,3,4,5], [6,7,8,9,10]])
print(y[0,1])
#accessing element on 2nd row, 5th column
print(y[1,4])

#accessing a 3-D array,  third element of the second array of the first array
z=numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(z[0,1,2])

#-ve indexing;the last element of the 2nd array
m=numpy.array([[1,2,3,4,5], [6,7,8,9,10]])
print(m[-1,-1])