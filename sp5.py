#sparse matrix methods
#Viewing stored data (not the zero items) with the data property
import numpy
from  scipy.sparse import csr_matrix

a=numpy.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(a).data)

#Counting nonzeros with the count_nonzero() method:
b=numpy.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(b).count_nonzero())

#Removing zero-entries from the matrix with the eliminate_zeros() method:
c=numpy.array([[0,0,0],[0,0,1],[1,0,2]])
d=csr_matrix(c)
d.eliminate_zeros()
print(d,'\n\n')

#Eliminating duplicate entries with the sum_duplicates() method:
e=numpy.array([[0,0,0],[0,0,1],[1,0,2]])
d=csr_matrix(e)
d.sum_duplicates()
print(d,'\n\n')

#Converting from csr to csc with the tocsc() method:
f=numpy.array([[0,0,0],[0,0,1],[1,0,2]])
g=csr_matrix(f)
g.tocsc()
print(g)