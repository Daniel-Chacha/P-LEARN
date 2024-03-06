#hierarchical clustering  ;unsupervised learning method for clustering data points
#requires us to decide on both a distance and linkage method. We will use euclidean distance and the Ward linkage method, which attempts to minimize the variance between clusters
#Now we compute the ward linkage using euclidean distance, and visualize it using a dendrogram:
import numpy
from matplotlib import pyplot
from scipy.cluster.hierarchy import dendrogram,linkage

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data=list(zip(x,y))
linkage_data=linkage(data,method='ward',metric='euclidean')
dendrogram(linkage_data)

pyplot.show()
