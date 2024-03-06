#zipf distribution
#Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
#a - distribution parameter.
#size - The shape of the returned array.
from matplotlib import pyplot
from numpy import random
import seaborn

a=random.zipf(a=2,size=(2,3))
print(a)


#visualization of zipf dist.
x=random.zipf(a=2,size=1000)
seaborn.distplot(x[x<10],kde=False)
pyplot.show()