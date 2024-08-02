import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3],[5,7,4])
plt.show()

x=[1,2,3]
y=[5,7,4]
plt.plot(x,y,label="first line")
x2=[1,2,3]
y2=[10,11,14]
plt.plot(x2,y2,label="second line")
plt.xlabel("plot number")
plt.ylabel("important variables")
plt.title("new graph")
plt.legend()
plt.show
 
'''
t=np.arrange(0.0,20.0,1)
s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s2=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
plt.subplot(2,1,1)
plt.plot(t,s)
plt.ylabel("value")
plt.title("first chart")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t,s2)
plt.xlabel("item"(s))
plt.show()
'''



 













