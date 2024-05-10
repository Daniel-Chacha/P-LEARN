#predict future event
#Now we can use the information we have gathered to predict future values.
#Example: Let us try to predict the speed of a car that passes the tollbooth at around the time 17:00:
#To do so, we need the same mymodel array from the example above
#Predict the speed of a car passing at 17:00:
import numpy


a= [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
b = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

c=numpy.poly1d(numpy.polyfit(a,b,3))
speed=c(17)
print(speed)