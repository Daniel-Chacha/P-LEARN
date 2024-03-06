#visualization of uniform distribution
import seaborn
from numpy import random
from matplotlib import pyplot

a=random.uniform(size=1000)
seaborn.distplot(a,hist=True)
pyplot.show()