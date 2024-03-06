import pandas as pd
child1={
    'name':'Emil',
    'year':2004
}
child2={
    'name':'Tobias',
    'year':2007
}
child3={
    'name':'Linus',
    'year':2011
}

myfamily={
    'child1':child1,
    'child2':child2,
    'child3':child3
}
print(myfamily)

print('\n\n')
#to access items in a nested dictionary,you use the names of the dictionaries,starting with the outer dictionary
#print(myfamily['child2']['name'])

x=pd.DataFrame(myfamily)

print(x)