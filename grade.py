a=int(input('Enter the mark for computer: '))
b=int(input('Enter the mark for chemistry: '))
c=int(input('Enter the mark for Mathematics: '))

total=a+b+c
avg=total/3
print('The total marks is: ',total)
print('The average mark is: ',avg)

if avg>=0 and avg<=100:
    if avg>=80:
        grade='A'
        print('Grade is ',grade)
    elif avg>=70:
        grade='B'
        print("Grade is ",grade)
    elif avg>=60:
        grade='C'
        print('Grade is ',grade )
    elif avg>=50:
        grade='D'
        print('Grade is ',grade)
    elif avg>=40:
        grade='E'
        print('Grade is ',grade)
    else:
        grade='F'
        print('Grade is ',grade)
else:
    print('Wrong marks entered!')

