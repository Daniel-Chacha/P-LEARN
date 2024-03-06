#created matrix
import numpy
from sklearn import metrics

actual=numpy.random.binomial(1,.9,1000)
predicted=numpy.random.binomial(1,.9,1000)

Accuracy=metrics.accuracy_score(actual,predicted) #(True Positive + True Negative) / Total Predictions
print(Accuracy)