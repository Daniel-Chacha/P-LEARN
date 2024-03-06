#creating pie charts using 'pie()'
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])

pyplot.pie(x)
pyplot.show()