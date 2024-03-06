#emphasizing each points with a specified marker
from matplotlib import pyplot
import numpy

ypoints=numpy.array([3,8,1,10])

pyplot.plot(ypoints, marker='*')
pyplot.show()