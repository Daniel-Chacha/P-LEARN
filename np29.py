#random distribution
from numpy import random
#Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
a=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(100))
print(a, "\n")

#a 2D array with 3 rows and 5 values
b=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(3,5))
print(b)