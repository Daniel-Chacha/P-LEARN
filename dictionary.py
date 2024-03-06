thisdict={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
print(thisdict)

print('\n\n')
#print the brand of the dictionary
print(thisdict['brand'])

print('\n\n')
#duplicates not allowed as duplicate values will overwrite the existing values
thisdict={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964',
    'year':'2023'
}
print(thisdict)
print(len(thisdict))

print('\n\n')
#using the dict() constructor to make a dictionary
thisdict=dict(name='John',age='36',country='Kenya')
print(thisdict)