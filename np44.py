#logistic distribution
# used to describe growth.
#loc - mean, where the peak is. Default 0.
#scale - standard deviation, the flatness of distribution. Default 1.
#size - The shape of the returned array.
from numpy import random
a=random.logistic(loc=1,scale=2,size=(2,3))
print(a)