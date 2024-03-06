#enumerated iteration using 'ndenumerate()'
#enumeration means mentioning sequence number of somethings one by one
import numpy
a=numpy.array([1,2,3])

for b, x in numpy.ndenumerate(a):
    print(b,x)