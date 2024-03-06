#visualization of poisson distribution
import seaborn
from matplotlib import pyplot
from numpy import random

x=random.poisson(lam=2,size=1000)
seaborn.distplot(x,kde=False)
pyplot.show()