#The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
import seaborn
from numpy import random
from matplotlib import pyplot

seaborn.distplot(random.binomial(n=100,p=0.5,size=1000),hist=False,label='binomial')
seaborn.distplot(random.normal(loc=50,scale=5,size=1000),hist=False,label='normal')
pyplot.show()