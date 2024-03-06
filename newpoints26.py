#multiple graphs with titles with a supertitle using the parameter 'suptitle()
from matplotlib import pyplot
import numpy
#graph 1
x=numpy.array([0, 1, 2, 3])
y=numpy.array([3, 8, 1, 10])

pyplot.subplot(1,2,1)
pyplot.title('Sales')
pyplot.plot(x,y)

#graph 2
x=numpy.array([0, 1, 2, 3])
y=numpy.array([10, 20, 30, 40])

pyplot.subplot(1,2,2)
pyplot.title('Income')
pyplot.plot(x,y)

pyplot.suptitle('MY SHOP')
pyplot.show()