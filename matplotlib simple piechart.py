import matplotlib.pyplot as plt
# Data for the pie chart
labels = ['Label A', 'Label B', 'Label C', 'Label D']
sizes = [30, 25, 20, 25]

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue', 'yellow'])

# Adding title
plt.title('Pie Chart Example')

# Display the pie chart
plt.show()
 
