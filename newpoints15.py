#drawing multiple lines by specifying both x and y axis points
from matplotlib import pyplot
import numpy

y1=([3,8,1,10])
x1=([0,1,2,3])
y2=([10,1,7,3])
x2=([0,1,2,3])

pyplot.plot(x1,y1,x2,y2)
pyplot.show()