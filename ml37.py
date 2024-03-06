#prediction
#How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x=x[:80]
train_y=y[:80]

test_x=x[80:]
test_y=y[80:]

z=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
s=z(5)
print(s)