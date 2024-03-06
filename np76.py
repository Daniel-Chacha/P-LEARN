#scatter
import pandas
from matplotlib import pyplot
a=pandas.read_csv('data1.csv')

a.plot(kind='scatter',x='Duration',y='Calories')
pyplot.show()