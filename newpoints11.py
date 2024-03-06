#using the keyword argument linestyle abb. as 'ls' to change style of plotted line
from matplotlib import pyplot
import numpy

ypoints=([3,8,1,10])

pyplot.plot(ypoints,ls='--')
pyplot.show()