#splitting 2D array into three 2D arrays
import numpy
a=numpy.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
b=numpy.array_split(a,3)
print(b,'\n\n')


#2D array into three 2D array
c=numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
d=numpy.array_split(c,3)
print(d,'\n\n')

#u can also specify the axis
c=numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
d=numpy.array_split(c,3,axis=1)
print(d,'\n\n')

#alternatively hsplit() can be used
c=numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
d=numpy.hsplit(c,3)
print(d)


#similar alternates of vstack() and dstack() are available as vsplit() and dsplit()