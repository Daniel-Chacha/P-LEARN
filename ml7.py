from matplotlib import pyplot
import numpy

x=numpy.random.normal(5,1,1000)
y=numpy.random.normal(10,2,1000)

pyplot.scatter(x,y)
pyplot.show()