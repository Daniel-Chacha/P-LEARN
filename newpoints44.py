#specifying the startangle using 'startangle' parameter
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])
mylabels=['Apples','Mangoes','Oranges','Pineapples']

pyplot.pie(x,labels=mylabels,startangle=90)
pyplot.show()