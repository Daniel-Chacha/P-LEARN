#confusion matrix ;It is a table that is used in classification problems to assess where errors in the model were made.
#The rows represent the actual classes the outcomes should have been. While the columns represent the predictions we have made. Using this table it is easy to see which predictions are wrong.
from matplotlib import pyplot
import numpy
from sklearn import metrics

#generate the numbers for "actual" and "predicted" values.
actual=numpy.random.binomial(1,.9,size=1000)
predicted=numpy.random.binomial(1,.9,size=1000)

#Once metrics is imported we can use the confusion matrix function on our actual and predicted values.
confusion_matrix=metrics.confusion_matrix(actual,predicted)

#To create a more interpretable visual display we need to convert the table into a confusion matrix display.
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,display_labels=[False,True])
cm_display.plot()
pyplot.show()