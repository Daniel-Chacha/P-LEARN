#Normality Tests (Skewness and Kurtosis)
#Normality tests are based on the skewness and kurtosis.
#The normaltest() function returns p value for the null hypothesis:
#Skewness: A measure of symmetry in data.,For normal distributions it is 0.
    #If it is negative, it means the data is skewed left.
     #If it is positive it means the data is skewed right.
#Kurtosis:A measure of whether the data is heavy or lightly tailed to a normal distribution.
     #Positive kurtosis means heavy tailed.
      #Negative kurtosis means lightly tailed.

import numpy
from scipy.stats import skew,kurtosis
v=numpy.random.normal(size=100)

print(skew(v))
print(kurtosis(v))