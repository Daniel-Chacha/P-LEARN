#Predict the CO2 emission from a 1300 liter car that weighs 2300 kilograms:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

a=pandas.read_csv('data2.csv')
x=a[['Weight','Volume']]
y=a['CO2']

b=scale.fit_transform(x)

c=linear_model.LinearRegression()
c.fit(b,y)

d=scale.transform([[2300,1300]])
predictedCO2=c.predict([d[0]])

print(predictedCO2)