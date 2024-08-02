#import pandas as pd
import matplotlib.pyplot as plt
'''
plt.plot([1,2,3],[5,7,4])
plt.show()

x=[2,4,6]
y=[7,4,8]
plt.plot(x,y,label='TOWN A')
x1=[7,8,3]
y1=[5,9,4]
plt.plot(x1,y1,label='TOWN B')
plt.legend()
plt.show()


y_axis=[20,50,15]
x_axis=[13,23,34]
plt.bar(x_axis,y_axis)
plt.show()
'''
data=[5,15,25,35,45,55]
plt.hist(data,
         bins=[0,10,20,30,40,50,60],
         weights=[20,10,45,33,6,8],
         edgecolor='red')
plt.show()








