#Of all the positive cases, what percentage are predicted positive?
#Sensitivity (sometimes called Recall) measures how good the model is at predicting positives.
#This means it looks at true positives and false negatives (which are positives that have been incorrectly predicted as negative).
#How to Calculate
#True Positive / (True Positive + False Negative)
#Sensitivity is good at understanding how well the model predicts something is positive:
import numpy
from sklearn import metrics

actual=numpy.random.binomial(1,.9,1000)
predicted=numpy.random.binomial(1,.9,1000)

Sensitivity_recall=metrics.recall_score(actual,predicted)
print(Sensitivity_recall)