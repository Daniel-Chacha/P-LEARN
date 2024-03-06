#creating a simple pandas from a dictionary
import pandas
a={'day1':'400','day2':'420','day3':'430','day4':'440'}
b=pandas.Series(a)
print(b)


print('\n\n')
#to select only a few items from the dictionary;day1 and day3
a={'day1':'400','day2':'420','day3':'430','day4':'440'}
b=pandas.Series(a,index=['day1','day3'])
print(b)

