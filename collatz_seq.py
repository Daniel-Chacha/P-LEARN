#has one parameter named number. If
#number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps
#calling collatz() on that number until the function returns the value 1.

def collatz(x):
    if x%2==0:
        y=x//2
    else:
        y=3* x +1

    return y

des=int(input('Enter a number: '))
m=collatz(des)
print(m)

while  m!=1:
    m=collatz(m)
    print(m)
 
