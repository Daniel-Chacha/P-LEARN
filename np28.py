#generating random numbers ; can't be predicted logically
from numpy import random
a=random.randint(100)  #a random integer
print(a)

b=random.rand()  #a random float
print(b)

c=random.randint(100,size=5) #a random array
print(c)

d=random.randint(100,size=(2,3)) #a random 2D array
print(d)

e=random.randint(100,size=(2,3,2)) # a random 3D array
print(e)

f=random.rand(5)  #a random 1D array with float numbers
print(f)

g=random.rand(3,5)  # a 2D array
print(g)

#generate random number from an array
h=random.choice([3,5,7,9,6])
print(h)

#generate an array from another array
g=random.choice([4,3,5,2,6],size=(3,5))
print(g)