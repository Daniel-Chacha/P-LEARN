#Bring in the Testing Set
#Now we have made a model that is OK, at least when it comes to training data.
#Now we want to test the model with the testing data as well, to see if gives us the same result.
#Let us find the R2 score when using testing data:

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150, 40, 100)/x

train_x=x[:80]
train_y=y[:80]

test_x=x[80:]
test_y=y[80:]

mymodel=numpy.poly1d(numpy.polyfit(train_x,train_y,4))
r2=r2_score(test_y, mymodel(test_x))
print(r2)