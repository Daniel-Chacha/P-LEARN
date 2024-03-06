#R squared
#It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.
#The relationship is measured with a value called the r-squared.
#The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
#Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

z=numpy.poly1d(numpy.polyfit(x,y,3))
m=r2_score(y,z(x))
print(m)
# The result 0.94 shows that there is a very good relationship, and we can use polynomial regression in future predictions