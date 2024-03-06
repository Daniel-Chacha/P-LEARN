#specificity ;How well the model is at prediciting negative results?
#Specificity is similar to sensitivity, but looks at it from the persepctive of negative results.
#How to Calculate
#True Negative / (True Negative + False Positive)
#Since it is just the opposite of Recall, we use the recall_score function, taking the opposite position label:
import numpy
from sklearn import metrics

actual=numpy.random.binomial(1,.9,1000)
predicted=numpy.random.binomial(1,.9,1000)

specificity=metrics.recall_score(actual,predicted,pos_label=0)
print(specificity)