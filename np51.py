#Pareto distribution
#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
#a - shape parameter.
#size - The shape of the returned array.
from matplotlib import pyplot
from numpy import random
import seaborn

d=random.pareto(a=2,size=(2,3))
print(d)

#visualization of pareto distribution
seaborn.distplot(random.pareto(a=2,size=1000),kde=False)
pyplot.show()