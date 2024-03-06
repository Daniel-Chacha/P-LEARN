#The depth_first_order() method returns a depth first traversal from a node.
#This function takes following arguments:
#the graph.
#the starting element to traverse graph from.

#Traverse the graph depth first for given adjacency matrix:
import numpy
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

a=numpy.array([
      [0, 1, 0, 1],
      [1, 1, 1, 1],
      [2, 1, 1, 0],
      [0, 1, 0, 1]
])
b=csr_matrix(a)
c=depth_first_order(b,1)
print(c,'\n\n')

#The breadth_first_order() method returns a breadth first traversal from a node.
#This function takes following arguments:
#the graph.
#the starting element to traverse graph from.

import numpy
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
a=numpy.array([
      [0, 1, 0, 1],
      [1, 1, 1, 1],
      [2, 1, 1, 0],
      [0, 1, 0, 1]
])

d=csr_matrix(a)
e=breadth_first_order(d,1)
print(e)