#working with matlab arrays
#SciPy provides us with the module scipy.io, which has functions for working with Matlab array
#The savemat() function allows us to export data in Matlab format.
#The method takes the following parameters:
#filename - the file name for saving data.
#mdict - a dictionary containing the data.
#do_compression - a boolean value that specifies whether to compress the result or not. Default False.

#Export the following array as variable name "vec" to a mat file:
from scipy import io
import numpy
a=numpy.array([0,1,2,3,4,5,6,7,8,9])

#export
io.savemat('arr.mat',{'vec':a})
#import  ;The loadmat() function allows us to import data from a Matlab file.
b=io.loadmat('arr.mat')
print(b,'\n\n')

#to display only the array
print(b['vec'])



print('\n\n')
#Note: We can see that the array originally was 1D, but on extraction it has increased one dimension.
#In order to resolve this we can pass an additional argument squeeze_me=True:
c=io.loadmat('arr.mat',squeeze_me=True)
print(c)