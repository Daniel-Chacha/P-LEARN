#difference btwn poisson and binomial distribution
#Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
#But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
import seaborn
from matplotlib import pyplot
from numpy import random

a=random.poisson(lam=10,size=1000)
b=random.binomial(n=1000,p=0.1,size=10000)

seaborn.distplot(a,hist=False,label='Poisson')
seaborn.distplot(b,hist=False,label='Binomial')

pyplot.show()

#output is false