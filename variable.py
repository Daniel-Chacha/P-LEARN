x='awesome'

def myfunc():
    print('Python is ' +x)

myfunc()

print('---------------------------------------------------------')
x='awesome'

def myfunc():
    x='fantastic'
    print('Python is '+x)

myfunc()
print('Python is '+x)

print('------------------------------------------------')
#how to make a variable global using the global keyword
def myfunc():
    global x
    x='fantastic'

myfunc()
print('Python is '+x)

print('-----------------------------------------------')
x='awesome'
def myfunc():
    global x
    x='fantastic'
    print('Python is',x)

myfunc()











    