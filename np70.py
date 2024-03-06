import pandas
a={
    'calories':[400,435,600,563],
    'duration':[50,40,35,68]
}
b=pandas.DataFrame(a)
print(b)

print('\n\n')
#locate a row  ;loc attribute is used ;returns a series
print(b.loc[0])

print('\n\n')
#return 1,2 row   ;[[]] return a dataframe
print(b.loc[[0,2]])