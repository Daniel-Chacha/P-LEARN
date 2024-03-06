#scipy graphs
#connected components ;Find all of the connected components with the connected_components() method.
import numpy
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

a=numpy.array([
    [0,1,2,],
    [1,0,0],
    [2,0,0]
])
b=csr_matrix(a)
print(connected_components(b))