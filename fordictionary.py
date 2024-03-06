#print all keys
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}
for x in car:
    print(x)

print('\n\n')
#print all values in the dictionary
for x in car:
    print(car[x])

print('\n\n')
#values() method returns values of the dictionary
for x in car.values():
    print(x)

print('\n\n')
#keys() methodreturns the keys of the dictionary
for x in car.keys():
    print(x)

print('\n\n')
#loop through both keys and values
for x,y in car.items():
    print(x,y)

