#train/test  ;method to measure the accuracy of your model.
#It is called Train/Test because you split the data set into two sets: a training set and a testing set.
#80% for training, and 20% for testing.
#You train the model using the training set.
#You test the model using the testing set.
#Train the model means create the model.
#Test the model means test the accuracy of the model.

#Start With a Data Set
#Start with a data set you want to test.
#Our data set illustrates 100 customers in a shop, and their shopping habits.

import numpy
from matplotlib import pyplot
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)           #The x axis represents the number of minutes before making a purchase.
y=numpy.random.normal(150,40,100)/x       #The y axis represents the amount of money spent on the purchase

pyplot.scatter(x,y)
pyplot.show()