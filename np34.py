#visualization of normal distribution
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.
from numpy import random
from matplotlib import pyplot
import seaborn

x=random.normal(size=1000)
seaborn.displot(x, kind='kde')
pyplot.show()