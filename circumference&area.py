pi=3.142
def circumference(radius):
    return 2*pi*radius

def area(radius):
    return pi*(pow(radius,2))

a=input('Enter the radius of the circle ')
r=int(a)
c =circumference(r)
a=area(r)

print('The circumference of the circle is ',c)
print('The area of the circle is ',a)