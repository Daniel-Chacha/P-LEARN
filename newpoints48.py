#to add a list of explanation use 'legend()' function
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])
mylabels=['Apples','Mangoes','Oranges','Pineapples']

pyplot.pie(x,labels=mylabels)
pyplot.legend()
pyplot.show()