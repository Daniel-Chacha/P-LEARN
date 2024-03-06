#creating bars
from matplotlib import pyplot
import numpy

x=numpy.array(['A','B','C','D'])
y=numpy.array([3, 8, 1, 10])

pyplot.bar(x,y)
pyplot.show()
