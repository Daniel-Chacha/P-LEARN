#different color for each point
from matplotlib import pyplot
import numpy

x = numpy.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = numpy.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = numpy.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
pyplot.scatter(x,y,c=colors)
pyplot.show()