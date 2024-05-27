#radar chart
import matplotlib.pyplot as plt
import numpy 


labels=numpy.array(['A','B','C','D','E'])
data=numpy.array([4,5,3,4,2])

angles=numpy.linspace(0,2*numpy.pi , len(labels),endpoint=False)
data=numpy.concatenate((data,[data[0]]))
angles=numpy.concatenate((angles,[angles[0]]))

plt.polar(angles, data,marker='o')
plt.fill(angles,data,alpha=0.25)
plt.title('Radar Chart')
plt.show()