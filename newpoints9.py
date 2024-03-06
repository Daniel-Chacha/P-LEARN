#setting the marker colour using the keyword argument 'markeredgecolour' abb. as 'mec'
from matplotlib import pyplot
import numpy

ypoint=([3,8,1,10])

pyplot.plot(ypoint,'o-g',ms=10,mec='r')
pyplot.show()