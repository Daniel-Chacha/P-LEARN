#polynomial regression  ;18 cars ,time passing in hours and their speed
from matplotlib import pyplot
import numpy

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
myline=numpy.linspace(1,22,100)

pyplot.scatter(x,y)
pyplot.plot(myline,mymodel(myline))
pyplot.show()
