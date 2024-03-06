#max rows that the system can display
import pandas
print(pandas.options.display.max_rows)

#In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
#You can change the maximum rows number with the same statement.

pandas.options.display.max_rows=9999
x=pandas.read_csv('data1.csv')
print(x)