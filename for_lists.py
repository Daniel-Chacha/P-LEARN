thislist=['apple', 'banana','cherry']
for x in thislist:
    print(x)

print('-------------------------------------------\n')
#loop through the index of numbers
thislist=['apple', 'banana','cherry']
for i in range (len(thislist)):
    print(thislist[i])

print('-------------------------------------\n')
# a shorthand for loop that will print all items in the list
thislist=['apple', 'banana','cherry']
[print(x) for x in thislist]
