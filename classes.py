#a class is an object constructor or a 'blueprint' for creating objects
#to create a class, use the keyword class
class myclass:
    x=5

p1=myclass()
print(p1.x)

print('\n\n')
#using the _init_() function to assign values
#create a class named person and use the _init_() function to assign values for name and age
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('John',36)
print(p1.name)
print(p1.age)

print('\n\n')
#the __str__() function controls what should be returned when the class object is represented as a string
#the string representation of an object WITHOUT  the __str__ function
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('John',36)
print(p1)


print('\n\n')
#the string representation of an object WITH  the __str__ function
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"

p1=person('John',36)
print(p1)

print('\n\n')
#insert a function that prints a greeting and execute it on the p1 object
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def myfunc(self):
        print('Hello my name is ',self.name)
    
p1=person('John',36)
p1.myfunc()


print('\n\n')
#the self parameter is used to access variables that belong to a class
#it does not have to be called self,you can call it whatever you like,but it has to be the first parameter of any function in a class
class person:
    def __init__(x,name,age):
        x.name=name
        x.age=age
    
    def myfunc(y):
        print('Hello my name is ',y.name)
    
p1=person('John',36)

p1.myfunc()


print('\n\n')
#modify object properties
class person:
    def __init__(x,name,age):
        x.name=name
        x.age=age
    
    def myfunc(y):
        print('Hello I am  ',y.age)
    
p1=person('John',36)
p1.age=40
p1.myfunc()

print('\n\n')
#delete object properties using the del keyword
class person:
    def __init__(x,name,age):
        x.name=name
        x.age=age
    
    def myfunc(y):
        print('Hello I am  ',y.age)
    
p1=person('John',36)
del p1.age
print(p1.age)
