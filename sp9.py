#spatial data; data that is represented in a geometric space
#SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.
#One method to generate these triangulations through points is the Delaunay() Triangulation.

#Create a triangulation from following points:
import numpy
from matplotlib import pyplot
from scipy.spatial import Delaunay

a=numpy.array([
      [2, 4],
      [3, 4],
      [3, 0],
      [2, 2],
      [4, 1]
])
h=Delaunay(a).simplices

pyplot.triplot(a[:,0],a[:,1],h)
pyplot.scatter(a[:,0],a[:,1],c='r')
pyplot.show()