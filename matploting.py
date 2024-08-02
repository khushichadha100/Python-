
import matplotlib.pyplot as plt
 
 # initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]
# plotting the data
 
plt.plot(x,y,marker="d",label="cgpa",linewidth=5)
# Adding the title
plt.title("line graph")
# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.legend()
plt.show()
 


import matplotlib.pyplot as plt 
# data to display on plots 
x = [2, 4, 6, 10]
y = [5, 2, 7, 9] 
# This will plot a simple bar chart
plt.bar(x, y,color='k',linewidth=8,label="bar")
# Title to the plot
plt.title("Bar Chart")
# Adding the legends
plt.legend()
plt.show()


import matplotlib.pyplot as plt 
# data to display on plots 
x = [2, 5, 8, 12 ] 
y = [4, 7, 9, 4 ] 
# This will plot a simple bar chart
plt.barh(x, y,color='k' ,edgecolor='cyan')
# Title to the plot
plt.title("Bar Chart")
# Adding the legends
plt.legend(["bar"])
plt.show()




import matplotlib.pyplot as plt
# Data labels, sizes, and colors are defined:
labels = ['Broccoli', 'Chocolate Cake', 'Blueberries', 'Raspberries']
sizes = [5,45,35,15]
explode=(0,0.1,0,0)
# Data is plotted:

plt.pie(sizes, labels=labels,autopct='%1.1f%%' ,shadow=True,explode=explode,
        colors = ['green', 'brown', 'skyblue', 'orange'])
#plt.legend(['Broccoli', 'Chocolate Cake', 'Blueberries', 'Raspberries'])
plt.title("pie plot")
plt.show()






















