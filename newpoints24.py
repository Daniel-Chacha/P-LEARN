#mutiple graphs on each other
from matplotlib import pyplot
import numpy
#graph 1
x=numpy.array([0, 1, 2, 3])
y=numpy.array([3, 8, 1, 10])

pyplot.subplot(2,2,1)
pyplot.bar(x,y)

#graph 2
x=numpy.array([0, 1, 2, 3])
y=numpy.array([10, 20, 30, 40])

pyplot.subplot(2,2,2)
pyplot.bar(x,y)

#graph 3
x=numpy.array([0, 1, 2, 3])
y=numpy.array([10, 20, 30, 40])

pyplot.subplot(2,2,3)
pyplot.bar(x,y)
#graph 4
x=numpy.array([0, 1, 2, 3])
y=numpy.array([3, 8, 1, 10])

pyplot.subplot(2,2,4)
pyplot.bar(x,y)


pyplot.show()