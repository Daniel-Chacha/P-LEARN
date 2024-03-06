#exponential distribution
#describing time till next event 
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#size - The shape of the returned array.

from numpy import random
from matplotlib import pyplot
import seaborn

s=random.exponential(scale=2,size=(2,3))
print(s)


#visualization of exponential dist.
seaborn.distplot(random.exponential(size=1000),hist=False)
pyplot.show()