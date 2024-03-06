#statistical description of data
#n order to see a summary of values in an array, we can use the describe() function.
import numpy
from scipy.stats import describe

v=numpy.random.normal(size=100)
s=describe(v)
print(s)