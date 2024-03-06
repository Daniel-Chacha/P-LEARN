#setting properties for gridlines
from matplotlib import pyplot
import numpy

x=numpy.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=numpy.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


pyplot.title('Sports Watch Data')
pyplot.xlabel('Average Pulse')
pyplot.ylabel('Calories Burnage')
pyplot.plot(x,y)

pyplot.grid(c='darkred',lw='0.5',ls='--')
pyplot.show()