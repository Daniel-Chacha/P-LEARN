#rearranging elements in an array
import numpy
from numpy import random
a=numpy.array([1,2,3,4,5])
random.shuffle(a)
print(a)

#permutation()
b=numpy.array([5,6,7,8,9])
random.permutation(b)
print(b)