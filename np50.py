#Rayleigh distribution
#scale - (standard deviation) decides how flat the distribution will be default 1.0).
#size - The shape of the returned array.
from numpy import random
from matplotlib import pyplot
import seaborn

d=random.rayleigh(scale=2,size=(2,3))
print(d)

#visualization of rayleigh distribution
seaborn.distplot(random.rayleigh(size=1000),hist=False)
pyplot.show()