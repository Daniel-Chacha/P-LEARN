#slicing 2-D array
#1st element slice from index 1 to 4
import numpy
m=numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(m[0,1:4])

#for both elements return index 2
print(m[:,2])

#for both elements slice index 1 to 4(not included)
print(m[:,1:4])