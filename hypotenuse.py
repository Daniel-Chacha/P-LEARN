import math
def hypotenuse(base,height):
    return math.sqrt((pow(base,2))+(pow(height,2)))

b=input('Enter the base of the triangle:')
t=input('Enter the height of the triangle: ')

x=int(b)
y=int(t)
h=hypotenuse(x,y)
print('The hypotenuse of the triangle is ',h)
