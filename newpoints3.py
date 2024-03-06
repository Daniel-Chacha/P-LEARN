#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
from matplotlib import pyplot
import numpy

xpoints=numpy.array([1,2,6,8])
ypoints=numpy.array([3,8,1,10])

pyplot.plot(xpoints,ypoints)
pyplot.show()