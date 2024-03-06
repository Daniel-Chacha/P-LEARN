#sparse data ; s a data set where most of the item values are zero.
#SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
#CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
#CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
import  numpy
from scipy.sparse import csr_matrix

a=numpy.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(a))