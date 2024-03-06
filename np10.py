#copy ;The copy SHOULD NOT be affected by the changes made to the original array
import numpy
m=numpy.array([1,2,3,4])
n=m.copy()
m[0]= 10
print(m)
print(n)

#view; The view SHOULD be affected by the changes made to the original array
o=numpy.array([1,2,3,4])
p=o.view()
o[0]=42
print(o)
print(p)

#making changes to the view
#The original array SHOULD be affected by the changes made to the view
r=numpy.array([1,2,3,5,6])
s=r.view()
s[0]=20
print(r)
print(s)

#copy() owns the data while view() doesn't, to check this numpy has the attribute base that returns None if the array owns the data ,otherwise it returns iot refers the original object
t=numpy.array([1,2,3,4])
u=t.copy()
v=t.view()

print(u.base)
print(v.base)