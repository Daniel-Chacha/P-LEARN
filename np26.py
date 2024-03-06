#create an array to return only even elements
import numpy
a=numpy.array([2,65,7,23,4,6,9,70,46,44])
filter_arr=[]

for x in a:
    if x%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

b=a[filter_arr]
print(filter_arr)
print(b)