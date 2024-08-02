import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 50]
 
 
# Plotting the bar graph
plt.bar(categories,values, color='blue')
 
# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example')

# Display the bar graph
plt.show()

 

 