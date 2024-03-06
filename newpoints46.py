#adding a shadow to the pie
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])
mylabels=['Apples','Mangoes','Oranges','Pineapples']
myexplode=[0.2,0,0,0]

pyplot.pie(x,labels=mylabels,explode=myexplode,shadow=True)
pyplot.show()