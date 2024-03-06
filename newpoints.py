#to plot only the markers ,use the shortcut 'o'
from matplotlib import pyplot
import numpy

x_points=numpy.array([1,8])
y_points=numpy.array([3,10])

pyplot.plot(x_points,y_points,'o')
pyplot.show()