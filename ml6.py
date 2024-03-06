#creating a normal data distribution and create a histogram
from matplotlib import pyplot
import numpy

x=numpy.random.normal(5.0,1.0,100000)
pyplot.hist(x,100)
pyplot.show()

