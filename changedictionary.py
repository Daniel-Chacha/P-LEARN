car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
car['year']='2023'
print(car)


print('\n\n')
#update() method will update the dictionary with the items from the argument
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
car.update({'year':2020})
print(car)