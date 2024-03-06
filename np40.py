#difference between poisson and normal distribution
import seaborn
from numpy import random
from matplotlib import pyplot

a=random.normal(loc=50,scale=7,size=1000)
b=random.poisson(lam=50,size=1000)

seaborn.distplot(a,hist=False,label='Normal')
seaborn.distplot(b,hist=False,label='Poisson')

pyplot.show()