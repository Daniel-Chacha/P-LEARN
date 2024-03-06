#chi square distribution
# used as a basis to verify the hypothesis.
#df - (degree of freedom).
#size - The shape of the returned array.
from numpy import random
from matplotlib import pyplot
import seaborn

s=random.chisquare(df=2,size=(2,3))
print(s)

#visualization of chisquare
seaborn.distplot(random.chisquare(df=1,size=1000),hist=False)
pyplot.show()