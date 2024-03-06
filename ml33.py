#display the training set
from matplotlib import pyplot
import numpy
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x

train_x=x[:80]
train_y=y[:80]

test_x=x[80:]
test_y=y[80:]

pyplot.scatter(train_x,train_y)
pyplot.show() #it looks similar to the original drawing hence it seems to be a fair selection


#displaying the test dataset
pyplot.scatter(test_x,test_y)
pyplot.show()
#he testing set also looks like the original data set: