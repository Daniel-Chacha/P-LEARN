#KS test is used to check if given values follow a distribution.
#The function takes the value to be tested, and the CDF as two parameters.
import numpy
from scipy.stats import kstest

v=numpy.random.normal(size=100)
b=kstest(v,'norm')
print(b)