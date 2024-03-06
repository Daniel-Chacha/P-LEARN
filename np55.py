#adding the contents of two arrays
import numpy
x=numpy.array([1,2,3,4])
y=numpy.array([5,6,7,8])
z=numpy.add(x,y)
print(z)

#subtracting content of two arrays
a=numpy.array([30,40,50,60,70])
b=numpy.array([5,10,15,20,25])
z=numpy.subtract(a,b)
print(z)

#multiplication
m=numpy.multiply(a,b)
print(m)

#division
d=numpy.divide(a,b)
print(d)

#power
f=numpy.array([6,7,8,9])
g=numpy.array([2,3,4,5])
h=numpy.power(f,g)
print(h)

#return the remainder after division
k=numpy.mod(f,g) #remainder() will also work
print(k)

#both quotient and remainder
l=numpy.divmod(f,g)
print(l)

#return absolute value
m=numpy.array([-1,-5,-3,6,3,-4])
n=numpy.absolute(m) #abs() would also work
print(n)