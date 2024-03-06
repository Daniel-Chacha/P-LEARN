from numpy import random
from matplotlib import pyplot
z=random.normal(size=(2,3))
print(z)

y=random.normal(loc=1,scale=2,size=(2,3))
print(y)
pyplot.plot(y)
pyplot.show()