#creating a ufunc ;you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
#The frompyfunc() method takes the following arguments:
#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.
import numpy
def myadd(a,b):
    return a+b

sum=numpy.frompyfunc(myadd,2,1)
print(sum([1,2,3,4],[5,6,7,8]))