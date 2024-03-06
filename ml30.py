#scaling
#It can be difficult to compare the volume 1.0 with the weight 790, but if we scale them both into comparable values, we can easily see how much one value is compared to the other.
#There are different methods for scaling data, in this tutorial we will use a method called standardization.
#The standardization method uses this formula:
#z = (x - u) / s
#Where z is the new value, x is the original value, u is the mean and s is the standard deviation
#'standard scaler'does all this
#Scale all values in the Weight and Volume columns:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

a=pandas.read_csv('data2.csv')
x=a[['Weight','Volume']]

b=scale.fit_transform(x)
print(b)