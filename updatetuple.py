#changing an item in a tuple
x=('apple','banana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)

print(x)

print('----APPENDING AN ITEM IN A TUPLE--------')
#appending an item to a tuple 
#1. converting the tuple to a list, append the item and then convert the list to  a tuple
thistuple=('apple','banana','cherry')
y=list(thistuple)
y.append('orange')
thistuple=tuple(y)

print(thistuple)

#2.add tuple to tuple
thistuple=('apple','banana','cherry')
y=('orange',)
thistuple+=y

print(thistuple)

print('---REMOVING  AN ITEM IN A TUPLE--------')
thistuple=('apple','banana','cherry')
y=list(thistuple)
y.remove('apple')
thistuple=tuple(y)

print(thistuple)
print('---DELETING A TUPLE--------')
thistuple=('apple','banana','cherry')
del thistuple
print(thistuple)