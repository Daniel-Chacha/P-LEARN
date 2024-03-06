#Draw a polynomial regression line through the training data points
import numpy
from matplotlib import pyplot
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x

train_x=x[:80]
train_y=y[:80]

z=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
myline=numpy.linspace(0,6,100)

pyplot.plot(myline,z(myline))
pyplot.scatter(train_x,train_y)
pyplot.show()
