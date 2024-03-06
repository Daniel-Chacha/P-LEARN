#program for sum of the of squares of the first n natural numbers

b=int(input('Enter a number: '))
squares=[]

for x in range(b):
    c=x**2
    squares.append(c)

d=sum(squares)
print(d)