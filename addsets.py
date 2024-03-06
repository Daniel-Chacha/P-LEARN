#a set is unchangeable but new items can be added
thisset={'apple','banana','cherry'}
thisset.add('orange')
print(thisset)

print('\n\n')
#to add an item from another set into the current set, use the update() method
thisset={'apple','banana','cherry'}
tropical={'pineapple','mango','papaya'}
thisset.update(tropical)

print(thisset)

print('\n\n')
#the object in update() method does not have to be a set, it can be a any iterable object (tuples,lists,dictionaries)
thisset={'apple','banana','cherry'}
mylist=['kiwi','orange']
thisset.update(mylist)
print(thisset)