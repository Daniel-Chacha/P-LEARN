#combine color,size and alpha
from matplotlib import pyplot
import numpy

x=numpy.random.randint(100,size=(100))
y=numpy.random.randint(100,size=(100))
colors=numpy.random.randint(100,size=(100))
size=10*numpy.random.randint(100,size=(100))

pyplot.scatter(x,y,c=colors,s=size,alpha=0.5,cmap='nipy_spectral')
pyplot.colorbar()
pyplot.show()