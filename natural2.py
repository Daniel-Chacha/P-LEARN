#program to cube sum of the first n natural numbers
a=int(input('Enter a number: '))
b=[]

for x in range(a):
    b.append(x)

c=sum(b)
d=pow(c,3)
print(d)

