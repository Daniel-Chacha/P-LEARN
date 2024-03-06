#visualization of binomial distribution
import seaborn
from matplotlib import pyplot
from numpy import random

x=random.binomial(n=10,p=0.5,size=10)
seaborn.distplot(x,hist=True,kde=False)
pyplot.show()