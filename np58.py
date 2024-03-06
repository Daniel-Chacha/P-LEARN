#summation  ;Addition is done between two arguments whereas summation happens over n elements.
import numpy
a=numpy.array([1,2,3,4,5])
b=numpy.array([6,7,8,9,10])
c=numpy.sum([a,b])
print(c)

print('\n\n')

d=numpy.array([1,2,3])
e=numpy.array([1,2,3])
f=numpy.sum([d,e],axis=1)
print(f)

print('\n\n')

#cummulative sum  ; 'cumsum' ; partially adding elements in ana array
#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
g=numpy.array([1,2,3])
e=numpy.cumsum(g)
print(e)
