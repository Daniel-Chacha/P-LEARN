#poisson distribution
#lam - rate or known number of occurrences e.g. 2 for above problem.
#size - The shape of the returned array.
from numpy import random
x=random.poisson(lam=2,size=10)
print(x)