#changing transparency of dots
from matplotlib import pyplot
import numpy

x = numpy.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = numpy.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = numpy.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
pyplot.scatter(x,y,s=sizes,alpha=0.5)

pyplot.show()