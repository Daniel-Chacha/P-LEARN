fruits=['apple','banana','cherry','kiwi','mango']
newlist=[]

for x in fruits:
    if 'a' in x:
        newlist.append(x)
    
print(newlist)

print('===============================\n')
#using a list comprehension for the above task
fruits=['apple','banana','cherry','kiwi','mango']
newlist=[x for x in fruits if 'a' in x]
print(newlist)

print('===============================\n')
newlist=[x for x in fruits if x != 'apple']
print(newlist)

print('===============================\n')
newlist=[x.upper() for x in fruits]
print(newlist)

print('===============================\n')
newlist=['hello' for x in fruits]
print(newlist)

print('===============================\n')
newlist=[x if x !='banana' else 'orange' for x in fruits]
print(newlist)

print('===============================\n')
fruits=['apple','banana','cherry','kiwi','mango']
for x in fruits:
    if x != 'banana':
        newlist.append(x)
    else:
        newlist.append('orange')

print(newlist)