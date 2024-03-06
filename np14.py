#iterating arrays
import numpy
m=numpy.array([1,2,3,4,5])
for x in m:
    print(x)

#iterating in 2D
o=numpy.array([[1,2,3],[4,5,6]])
for x in o:
    print(x)

#to iterate on each scalar element of the 2D array
o=numpy.array([[1,2,3],[4,5,6]])
for x in o:
    for y in x:
        print(y)


#iterate on elements of a 3D array
a=numpy.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in a:
    print(x,'\n')

#iterate down to the scalars
a=numpy.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in a:
    for y in x:
        for z in y:
            print(z)