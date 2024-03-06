# dijkstra method is used to find shortest path from one element to the other
#It takes following arguments:
#return_predecessors: boolean (True to return whole path of traversal otherwise False).
#indices: index of the element to return all paths from that element only.
#limit: max weight of path.

#Find the shortest path from element 1 to 2:
import numpy
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

a=numpy.array([
    [0,1,2,],
    [1,0,0],
    [2,0,0]
])
b=csr_matrix(a)
c=dijkstra(b,return_predecessors=True,indices=0)
print(c,'\n\n\n')

#Use the floyd_warshall() method to find shortest path between all pairs of elements.
import numpy
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
a=numpy.array([
    [0,1,2,],
    [1,0,0],
    [2,0,0]
])
d=csr_matrix(a)
e=floyd_warshall(d,return_predecessors=True)
print(e,'\n\n\n')

#The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.
import numpy 
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
f=numpy.array([
    [0,-1,2,],
    [1,0,0],
    [2,0,0]
])
g=csr_matrix(f)
e=bellman_ford(g,return_predecessors=True,indices=0)
print(e)