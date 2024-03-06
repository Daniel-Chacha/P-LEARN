#creating histograms
from matplotlib import pyplot
import numpy
x=numpy.random.normal(170,10,250)

pyplot.hist(x)
pyplot.show()