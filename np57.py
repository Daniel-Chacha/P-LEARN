#logs 
import numpy
a=numpy.arange(1,10)
print(numpy.log2(a))

print('\n\n')

#log 10
a=numpy.arange(1,10)
print(numpy.log10(a))

print('\n\n')

#log base e
a=numpy.arange(1,10)
print(numpy.log(a))

print('\n\n')

#log ata any base
from math import log
b=numpy.frompyfunc(log,2,1)
print(b(100,15))