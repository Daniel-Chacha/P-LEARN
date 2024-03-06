# using +
list1=['a','b','c']
list2=[1,2,3]

list3=list1+list2
print(list3)

print('------------------------------\n')
# appending all elements of list1 to list2
for x in list2:
    list1.append(x)

print(list1)

print('------------------------------\n')
#using the extend() method
list1=['a','b','c']
list2=[1,2,3]

list1.extend(list2)
print(list1)