#return an iterator from a tuple
mytuple=('apple','banana','cherry')
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('\n\n')
#strings are also iterable objects,containing a sequence of characters

x='banana'
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

print('\n\n')
#create an iterator that returns numbers,starting with 1 and each sequence will increase by 1
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a +=1
        return x
    
myclass=mynumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('\n\n')
#the above program would continue forever if you had enough next() statements
#to stop the iteration , use Stopiteration statement
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a>=20:
            x=self.a
            self.a +=1
            return x
        
        else:
            raise StopIteration
    
myclass=mynumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)