#without specifying x axis points, default o,1,2,3,4 will be used
from matplotlib import pyplot
import numpy

ypoints=numpy.array([3, 8, 1, 10, 5, 7])

pyplot.plot(ypoints)
pyplot.show()