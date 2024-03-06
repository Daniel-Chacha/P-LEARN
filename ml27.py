#multiple regression  ;is like linear regression, but with more than one independent value,
# meaning that we try to predict a value based on two or more variables.
import pandas
from sklearn import linear_model

a=pandas.read_csv('data2.csv')
x=a[['Weight','Volume']]
y=a['CO2']

d=linear_model.LinearRegression()
d.fit(x,y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2=d.predict([[2300,1300]])

print(predictedCO2)