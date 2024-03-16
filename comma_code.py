'''Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'.'''

def comma(x):
    print(f'{x}')
    #print(m)
    for y in range(len(x)):
        print(x[y],sep=',',end='  ',)

spam=['apples','banana','mangoes','strawberry','lemons']
comma(spam)