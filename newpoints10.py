#setting the colour inside marker using the keyword argument 'markerfacecolour' abb. as 'mfc'
from matplotlib import pyplot

ypoint=([3,8,1,10])

pyplot.plot(ypoint,'o:r',ms=10,mec='g',mfc='b')
pyplot.show()