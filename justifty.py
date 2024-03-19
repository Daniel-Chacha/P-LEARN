# rjust() ,ljust() ,center()

a='Hello'
b=a.rjust(20)
print(b,'\n')

c='Hello World!'
d=c.rjust(20)
print(d,'\n\n')


#alternatively, a specific fill character can be specified rather than the default blank space
a='Hello'
b=a.rjust(20,'*')
print(b,'\n')

a='Hello'
b=a.rjust(20,'-')
print(b,'\n')

#ljust()
a='Hello'
b=a.ljust(20,'-')
print(b,'\n')

#center()
a='Hello'
b=a.center(20)
print(b,'\n')

a='Hello'
b=a.center(20,'=')
print(b,'\n')
