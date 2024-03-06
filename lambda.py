# syntax is  'lambda arguments:expression'
#add 10 to argument a , and return the result
x=lambda a:a+10
print(x(5))

print('\n\n')
#multiply argument a with argument b and return the result
x=lambda a,b: a*b
print(x(5,6))

print('\n\n')
#summarise argument a,b,c and return the result
x=lambda a,b,c :a+b+c
print(x(4,6,10))

print('\n\n')
# power of a lambda function is better shown when you use it as an anonymous function inside another function
#eg. a function that always double the number that is sent in
def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
print(mydoubler(11)) 

print('\n\n')
#a function that always triples the number it receives
def myfunc(n):
    return lambda a:a*n

mytripler=myfunc(3)
print(mytripler(11))

print('\n\n')
#use the same function to perform both operations
def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11))
print(mytripler(11))