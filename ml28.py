#Coefficient
#The coefficient is a factor that describes the relationship with an unknown variable.
#Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
#In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) 
    #we get tells us what would happen if we increase, or decrease, one of the independent values.

import pandas
from sklearn import linear_model

a=pandas.read_csv('data2.csv')
x=a[['Weight','Volume']]
y=a['CO2']

b=linear_model.LinearRegression()
b.fit(x,y)

print(b.coef_)