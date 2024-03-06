#viewing the data
#The head() method returns the headers and a specified number of rows, starting from the top.
import pandas
c=pandas.read_csv('data1.csv')
print(c.head(10))   #if the number of rows is not specified, the head() method will return the top 5 rows.

print('\n\n')
#viewing last columns
print(c.tail())

print('\n\n')
#more information about the data
print(c.info())