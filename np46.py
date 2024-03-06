#difference btwn logistic and normal distribution
#Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
import seaborn
from numpy import random
from matplotlib import pyplot

seaborn.distplot(random.logistic(size=1000),hist=False,label='Logistic')
seaborn.distplot(random.normal(scale=2,size=1000),hist=False,label='Normal')
pyplot.show()