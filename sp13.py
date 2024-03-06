#ciyblock distance / manhattan distance
#Is the distance computed using 4 degrees of movement.
#E.g. we can only move: up, down, right, or left, not diagonally.

#find distance between points
from scipy.spatial.distance import cityblock
p1=(1,0)
p2=(10,2)

x=cityblock(p1,p2)
print(x)

#cosine distance  ;Is the value of cosine angle between the two points A and B.
#Find the cosine distsance between given points:
from scipy.spatial.distance import cosine
p1=(1,0)
p2=(10,2)

y=cosine(p1,p2)
print(y)