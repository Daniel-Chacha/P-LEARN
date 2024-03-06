#when we create a tuple ,we normally assign values to it, this is called packing
fruits=('apple','banana','cherry')
(green,yellow,orange)=fruits
print(green)
print(yellow)
print(orange)

print('\n\n\n')

#if the number of variables is less than the number of values,add an * to the variable name and the values will be assigned to the variable as a list
fruits=('apple','banana','cherry','strawberry','raspberry')
(green,yellow,*orange)=fruits
print(green)
print(yellow)
print(orange)

print('\n\n\n')
fruits=('apple','banana','cherry','strawberry','raspberry')
(green,*yellow,orange)=fruits
print(green)
print(yellow)
print(orange)