#we can combine strings and numbers using the format() method i.e to insert a number into a string
age=36
txt='My name is John, and I am {}'
print(txt.format(age))
 

print('------------------------------------------')
quantity=3
itemno=567
price=49.95
myorder='I want {} pieces of item {} for {} Ksh'
print(myorder.format(quantity,itemno,price))

print('------------------------------------------')
#use of index numbersto be sure the arguments are placed in the correct placeholder
quantity=3
itemno=567
price=49.95
myorder='I want to pay {2} Ksh for {0} pieces of item {1}'
print(myorder.format(quantity,itemno,price))