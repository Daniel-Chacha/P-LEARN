#slicing arrays 
#2nd to 4th element
import numpy
m=numpy.array([1,2,3,4,5,6,7,8,9])
print(m[1:4])

#3rd to last element
print(m[2:])

#start to 5th element
print(m[:5])

#-ve slicing
#5th to 8th item
print(m[-5:-1])

#steps
print(m[1:8:2])

#skip by 2 the entire way
print(m[::2])