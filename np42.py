#uniform distribution; every event has equal chances of occurring
#a - lower bound - default 0 .0.
#b - upper bound - default 1.0.
#size - The shape of the returned array.

from numpy import random
a=random.uniform(size=(2,3))
print(a)