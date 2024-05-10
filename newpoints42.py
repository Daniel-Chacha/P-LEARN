#creating pie charts using 'pie()'
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])

#print(x)
pyplot.pie(x)
pyplot.show()