#setting colors for bars and width using keyword argument'width()'
from matplotlib import pyplot


x=(['A','B','C','D'])
y=([3, 8, 1, 10])

pyplot.bar(x,y,color='r',width=0.5)
pyplot.show()