#bad fit ;where linear regression would not be the best method to predict future values.
from matplotlib import pyplot
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope,intercept,r,p,std_err=stats.linregress(x,y)
def myfunc(x):
    return slope *x + intercept

y1=list(map(myfunc,x))
pyplot.scatter(x,y)
pyplot.plot(x,y1)
pyplot.show()

#r for relationship
print(r) #: 0.013 indicates a very bad relationship, and tells us that this data set is not suitable for linear regression.
