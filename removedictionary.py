car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
car.pop('brand')
print(car)


print('\n\n')
#popitem() method removes the last inserted item
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
car.popitem()
print(car)

print('\n\n')
#del keyword removes the item with the specified key name
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
del car['brand']
print(car)



print('\n\n')
#clear method empties the dictionary
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
car.clear()
print(car)

print('\n\n')
#del keyword can also be used to delete the whole dictionary
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
del car
print(car)