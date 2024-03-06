#r squared
#How well does my training data fit in a polynomial regression?
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x

train_x=x[:80]
train_y=y[:80]

z=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
a=r2_score(train_y,z(train_x))
print(a) #the result is ok
