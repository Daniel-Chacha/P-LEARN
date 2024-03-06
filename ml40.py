#precision
#Of the positives predicted, what percentage is truly positive?
#How to Calculate
#True Positive / (True Positive + False Positive)
#Precision does not evaluate the correctly predicted negative cases:
import numpy
from sklearn import metrics

actual=numpy.random.binomial(1,.9,1000)
predicted=numpy.random.binomial(1,.9,1000)

Precision=metrics.precision_score(actual,predicted)
print(Precision)