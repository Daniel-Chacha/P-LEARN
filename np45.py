#visualization of logistic distribution
import seaborn
from numpy import random
from matplotlib import pyplot

a=random.logistic(size=1000)
seaborn.distplot(a,hist=False)
pyplot.show()
