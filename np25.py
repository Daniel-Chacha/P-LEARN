#filtering arrays; is getting some elements out of an array and creating a new array out of them
#a boolean index list is used; if True that element is contained in th filtered array if False,the element is excluded from the filtered list

#create an array from the elements on index 0 and 2
import numpy
a=numpy.array([41,42,43,44])
x=[True,False,True,False]
b=a[x]
print(b,'\n\n')

#filter array
#create a filter array that will only return values greater than 42
d=numpy.array([41,42,45,34,65,78])
filter_arr=[]

for x in d:
    if x >=42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

e=d[filter_arr]
print(filter_arr)
print(e)