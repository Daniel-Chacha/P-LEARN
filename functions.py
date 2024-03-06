def myname(*name):
    print(name[0]+name[1])

myname('Daniel ','Chacha')

print('\n\n')
#ifyou do not know how many arguments will be passed into your function ,add an * before the parameter name in the function definition
def myfunc(*kids):
    print('The youngest child is ' + kids[2])

myfunc('Emilly','Tobias','Linus')

print('\n\n')
#arguments can also be sent using the key=value syntax
def myfunc(child3,child2,child1):
    print('The youngest child is: '+child3)

myfunc(child1='Emil',child2='Tobias',child3='Linus')


print('\n\n')
#if you do not know how many keyword arguments that will be passed into your function, add  ** before the parameter name in the function definition
def myfunc(**kids):
   print('His last name is ' +kids['lname'])

myfunc(fname='Tobias',lname='Jairo')

print('\n\n')
#using a default prameter value
def myfunc(country='Norway'):
    print('Iam from '+country)

myfunc('Sweden')
myfunc('Kenya')
myfunc()
myfunc('Brazil')

print('\n\n')
def myfunc(food):
    for x in food:
        print(x)

fruits=['apple','bananas','cherry']
myfunc(fruits)