# a heatmap
import seaborn , numpy
import matplotlib.pyplot as plt

data=numpy.random.rand(10,10)

seaborn.heatmap(data,annot=True)
plt.title('Heatmap')
plt.show()