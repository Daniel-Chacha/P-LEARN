#differences
#A discrete difference means subtracting two successive elements.
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
import numpy
a=numpy.array([10,15,25,5])
b=numpy.diff(a)
print(b)

#We can perform this operation repeatedly by giving parameter n.
#E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then,
# since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
c=numpy.array([10,15,25,5])
d=numpy.diff(c,n=2)
print(d)