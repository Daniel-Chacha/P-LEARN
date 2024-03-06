#setting the color for each wedge
from matplotlib import pyplot
import numpy
x=numpy.random.normal([35, 25, 25, 15])
mylabels=['Apples','Mangoes','Oranges','Pineapples']
mycolors=['red','green','blue','violet']

pyplot.pie(x,labels=mylabels,colors=mycolors)
pyplot.show()