#Hamming Distance
#Is the proportion of bits where two bits are different.
#It's a way to measure distance for binary sequences.
from scipy.spatial.distance import hamming
p1=(True,False, True)
p2=(False,True,True)

a=hamming(p1,p2)
print(a)

