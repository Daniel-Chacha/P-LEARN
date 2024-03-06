#only vertical grids
from matplotlib import pyplot
import numpy

x=numpy.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=numpy.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1={'family':'serif','color':'red','size':'16'}
font2={'family':'serif','color':'turquoise','size':'15'}

pyplot.title('Sports Watch Data',fontdict=font1)
pyplot.xlabel('Average Pulse',fontdict=font2)
pyplot.ylabel('Calories Burnage',fontdict=font2)
pyplot.plot(x,y)

pyplot.grid(axis='x')
pyplot.show()
