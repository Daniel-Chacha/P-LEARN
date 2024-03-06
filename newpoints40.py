#using horizontal bars ,height() in place of width()
from matplotlib import pyplot
import numpy

x=(['A','B','C','D'])
y=([3, 8, 1, 10])

pyplot.barh(x,y,height=0.5)
pyplot.show()