import numpy
from scipy import stats
from matplotlib import pyplot
#bad fit  ;hese values for the x- and y-axis should result in a very bad fit for polynomial regression:
a = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
b = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

c=numpy.poly1d(numpy.polyfit(a,b,3))
d=numpy.linspace(2,95,100)

pyplot.plot(d,c(d))
pyplot.scatter(a,b)
pyplot.show()

#R for relationship
from sklearn.metrics import r2_score
e=r2_score(b,c(a))
print(e)
#The result: 0.00995 indicates a very bad relationship, and tells us that this data set is not suitable for polynomial regression.