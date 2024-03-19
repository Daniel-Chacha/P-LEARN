
#while True:
    #age=input('Enter your age: ')
    #if age.isdecimal():
        #print(age)
        #break
    #print('Error!! Age can only be a number')

while True:
    print('Password must contain both numbers and letters (symbols are optional')
    password=input('Enter your password: ')
    if any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
        print(password)
        break
    print('Error!! ')