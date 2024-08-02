# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:32:12 2024

@author: lenovo 2020
"""

import csv

# CSV file write
file = open('csv_file.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Name', 'Age', 'City'])
writer.writerow(['John', 25, 'New York'])
file.close()

# CSV file read
file = open('csv_file.csv', 'r')
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()

# CSV file append/update
file = open('csv_file.csv', 'a', newline='')
writer = csv.writer(file)
writer.writerow(['Jane', 30, 'San Francisco'])
file.close()

# CSV file read after append/update
file = open('csv_file.csv', 'r')
 
reader = csv.reader(file)
print(reader)
file.close()
