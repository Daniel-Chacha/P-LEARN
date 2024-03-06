import pandas

a=pandas.read_csv('data1.csv')
print(a.to_string())    
#to_string() to print the entire DataFrame.
#without 'to_string' only the first 5 rows, and the last 5 rows will be returned


