#any value,string or number is true except empty string , a zero
print(10>9)
print(10==9)
print(10<9)

print("1--------------------------------------------")
print(bool('Hello'))
print(bool(15))

print("2--------------------------------------------")
x='Hello'
y=15
print(bool(x))
print(bool(y))

print("3--------------------------------------------")
(bool('abc'))
bool(123)
bool(['apple','cherry','banana'])

print("4-++-*++-*-*++-*-*-++*-*-*-*-*-*-*----")
#empty values such as (),[],{},"" , the number 0 , the value 'None' evaluate to false and an object that is made from a class with a '_ _len_ _' function that returns 0 o false

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print("5--------------------------------------------")
class myclass():
    def __len__(self):
        return 0
myobj =myclass()
print(bool(myobj))

print("6--------------------------------------------")
#a function that return  boolean
def myfunction():
    return True

print(myfunction())

print("7--------------------------------------------")
#a function that if YES it returns True otherwise print NO
def myfunction():
    return True

if myfunction():
    print('YES!')
else:
    print('NO')

# isinstance() ;an inbuilt function that returns a boolean value and can be used to determine if an object is of a certain data type
x=200
print(isinstance(x,int))
