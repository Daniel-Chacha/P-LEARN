#creating filter directly from array
import numpy
a=numpy.array([41,42,43,44])
filter_arr=a>42
b=a[filter_arr]

print(filter_arr)
print(b)

c=numpy.array([10,23,44,60,76,55,77,89,56])
d=c%2==0
e=c[d]

print(d)
print(e)