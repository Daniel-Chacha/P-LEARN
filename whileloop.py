i=1
while i<6:
    print(i)
    i+=1

print('\n\n')
#the break statement can be used to stop the loop even if the while condition is true
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

print('\n\n')
#continue statement is used to stop the current iteration and continue with the next
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


    
    
    