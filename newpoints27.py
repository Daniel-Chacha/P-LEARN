#the scatter() function plots one dot for each observation
from matplotlib import pyplot
import numpy

x = numpy.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = numpy.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

pyplot.scatter(x,y)
pyplot.show()