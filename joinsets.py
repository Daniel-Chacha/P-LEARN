#union() method return a new set containing all items from both sets
set1={'a','b','c'}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

print('\n\n')
#update() method inserts all items from one set into another
set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1)
#both union() and update() will exclude any duplicate values

print('\nONLY the duplicates\n')
#intersection_update() will keep only the items that are present in both sets
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.intersection_update(y)
print(x)

print('\n\n')
#intersection() metod will return a new set that contains the items in both sets
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.intersection(y)
print(z)

print('\n---all BUT not the duplicates----\n')
#symmetric_difference_update method, will keep only the elements that are not present in both sets
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.symmetric_difference_update(y)
print(x)

print('\n\n')
#symmetric_difference method will return a new set , that contains only the elements that are NOT present in both cases
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.symmetric_difference(y)
print(z)