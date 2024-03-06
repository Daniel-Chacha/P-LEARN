#polynomial regression
#If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

#In the example below, we have registered 18 cars as they were passing a certain tollbooth.
#We have registered the car's speed, and the time of day (hour) the passing occurred.
#The x-axis represents the hours of the day and the y-axis represents the speed
# a scatter
from matplotlib import pyplot
from scipy import stats
import numpy
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

z=numpy.poly1d(numpy.polyfit(x,y,3))
n=numpy.linspace(1,22,100)

pyplot.plot(n,z(n))
pyplot.scatter(x,y)
pyplot.show()