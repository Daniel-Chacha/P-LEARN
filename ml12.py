#badfit ;where polygression can't be applied to predict future occurrences
import numpy
from matplotlib import pyplot

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
myline=numpy.linspace(2,95,100)

pyplot.scatter(x,y)
pyplot.plot(myline,mymodel(myline))
pyplot.show()