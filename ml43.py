#F-score
#F-score is the "harmonic mean" of precision and sensitivity.
#It considers both false positive and false negative cases and is good for imbalanced datasets.
#How to Calculate
#2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
#This score does not take into consideration the True Negative values:
import numpy
from sklearn import metrics

actual=numpy.random.binomial(1,.9,1000)
predicted=numpy.random.binomial(1,.9,1000)

F1_score=metrics.f1_score(actual,predicted)
print(F1_score)