#making one of the edges to stand out from matplotlib import pyplot
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])
mylabels=['Apples','Mangoes','Oranges','Pineapples']
myexplode=[0.2,0,0,0]

pyplot.pie(x,labels=mylabels,explode=myexplode)
pyplot.show()