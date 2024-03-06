#create a set of data with 10000 numbers and create a histogram with 100 bars
from matplotlib import pyplot
import numpy

x=numpy.random.uniform(1,10,10000)
pyplot.hist(x,100)
pyplot.show()