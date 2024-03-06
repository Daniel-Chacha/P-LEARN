#to display the current date,import a module called 'datetime' to work with dates
import datetime

x=datetime.datetime.now()
print(x)

print('\n\n')
#to return weekday and year
print(x.strftime('%U'))
print(x.year)