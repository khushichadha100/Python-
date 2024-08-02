import matplotlib.pyplot as plt
import numpy as np
 
x=[4,6,8,10]
binss=[5,10,15,20]
y=[1,5,10,15]


plt.hist(y,weights=x,bins=binss,edgecolor="red",facecolor="y")

plt.show()


 