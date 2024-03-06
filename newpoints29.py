#setting color for each scatter
from matplotlib import pyplot
import numpy

x = numpy.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = numpy.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

pyplot.scatter(x,y,c='r')

x = numpy.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = numpy.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

pyplot.scatter(x, y,c='b')

pyplot.show()