#T-Test
#T-tests are used to determine if there is significant deference between means of two variables and lets us know if they belong to the same distribution
#Find if the given values v1 and v2 are from same distribution:
import numpy
from scipy.stats import ttest_ind

v1=numpy.random.normal(size=100)
v2=numpy.random.normal(size=100)

a=ttest_ind(v1,v2)
print(a,'\n\n')

#return only the pvalue
b=ttest_ind(v1,v2).pvalue
print(b)