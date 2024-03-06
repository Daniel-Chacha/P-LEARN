#The result array represents the coefficient values of weight and volume.
#Weight: 0.00755095
#Volume: 0.00780526
#These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
#And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
#I think that is a fair guess, but let test it!
#We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.
#What if we increase the weight with 1000kg?

#change the weight from 2300 to 3300
import pandas
from sklearn import linear_model

a=pandas.read_csv('data2.csv')
x=a[['Weight','Volume']]
y=a['CO2']

b=linear_model.LinearRegression()
b.fit(x,y)

predictedCO2=b.predict([[3300,1300]])
print(predictedCO2)

#We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.
#Which shows that the coefficient of 0.00755095 is correct:
#107.2087328 + (1000 * 0.00755095) = 114.75968