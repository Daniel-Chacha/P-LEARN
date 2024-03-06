#convex hull is the smallest polygon that covers all of the given points.
#Use the ConvexHull() method to create a Convex Hull.

import numpy
from scipy.spatial import ConvexHull
from matplotlib import pyplot

a=numpy.array([
      [2, 4],
      [3, 4],
      [3, 0],
      [2, 2],
      [4, 1],
      [1, 2],
      [5, 0],
      [3, 1],
      [1, 2],
      [0, 2]
])
b=ConvexHull(a).simplices
pyplot.scatter(a[:,0],a[:,1])

for simplex in b:
    pyplot.plot(a[simplex,0],a[simplex,1],'k-')

pyplot.show()