# a violin plot

import seaborn,numpy
import matplotlib.pyplot as plt

data=[numpy.random.normal(0,std,100) for std in range(1,4)]

seaborn.violinplot(data=data)
plt.title('Violin Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()