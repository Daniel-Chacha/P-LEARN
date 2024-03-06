thisdict={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
print(thisdict['model'])

print('\n\n')
#access a value using the get() method
thisdict={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
x=thisdict.get('model')
print(x)

print('\n\n')
#the keys()method will return  a list of all the keys in the dictionary
y=thisdict.keys()
print(y)

print('\n\n')
#adding a new item to a dictionary
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
x=car.values()
print(x)
car['colour']='blue'
print(x)

print('\n\n')
#items() method will return each item in a dictionary as tuples in a list
x=car.items()
print(x)