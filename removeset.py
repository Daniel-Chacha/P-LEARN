# using the remove() method;if the item does'nt exist , it will raise an error
thisset={'apple','banana','cherry'}
thisset.remove('apple')
print(thisset)

print('\n\n')
#using the discard() method;if the item doesn't exist it will not raise an error
thisset={'apple','banana','cherry'}
thisset.discard('apple')
print(thisset)

print('\n\n')
#using the pop() method; it removes a random object so you can't be sure what item gets removed
thisset={'apple','banana','cherry'}
x=thisset.pop()
print(thisset)

print('\n\n')
#the clear() method empties the set
thisset={'apple','banana','cherry'}
thisset.clear()
print(thisset)

print('\n\n')
#del keyword will delete the whole set
thisset={'apple','banana','cherry'}
del thisset
print(thisset)