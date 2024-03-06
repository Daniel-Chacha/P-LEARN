#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#dataframe in series is like table in excel
import pandas
x={
    'cars':['BMW','Volvo','Mercedes','Ferari','Lamborghini'],
    'passings':['3','7','4','9','3']
}
y=pandas.DataFrame(x)
print(y)

print('\n\n')
#a pandas series is like a column in a table
x=[1,7,4,6,3]
y=pandas.Series(x)
print(y)

print('\n\n')
#create my own labels ; items cann be accessed by reffering to the labels
x=[1,7,4,6,3]
y=pandas.Series(x,index=['x','y','z','m','n'])
print(y)
