#regression ; used when you try to find the relationship between variables
#Linear regression uses the relationship between the data-points to draw a straight line through all them
from matplotlib import pyplot
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x +intercept

y1=list(map(myfunc,x))

pyplot.scatter(x,y)
pyplot.plot(x,y1)
pyplot.show()
