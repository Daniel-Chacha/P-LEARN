import numpy as np
import matplotlib.pyplot as plt 

#define parameter t
t=np.linspace(0,39*np.pi/2,1000)

#define the equations for x and y 
x=t *np.cos(t)**3
y=9*t *np.sqrt(np.abs(np.cos(t))) +t* np.sin(0.2*t) *np.cos(4*t)

#define the segment indices and corresponding colors
segments= [
    (0, 200, 'orange'),
    (200,600, 'magenta'),
    (600 ,1000 , 'red')
]

#plot each segment separately with the corresponding color
for start , end , color in segments:
    plt.plot(x[start:end] ,y[start:end], c=color)

plt.show()