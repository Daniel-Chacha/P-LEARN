#finding the mean of a set of  numbers
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x=numpy.mean(speed)
print(x)

#finding the median of a set of numbers
y=numpy.median(speed)
print(y)





#finding the mode of a set of numbers
from scipy import stats
z=stats.mode(speed)
print(z)