import pandas as pd
# importing the csv module
import csv  
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1'],
         ['kabeer', 'EP', '2', '9.1']]
rows1 = [ ['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1']]
# name of csv file
filename = "university_records.csv"  
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    csvwriter.writerows(rows1)

with open(filename, 'a') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)   
    # writing the data rows
    csvwriter.writerows(rows)
    
rows2 = [ ['anamika', 'COE', '2','3.0'],
         ['Suraj', 'COE', '2', '9.1']]
    
with open(filename, 'a') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
       
    # writing the data rows
    csvwriter.writerows(rows2)

df=pd.read_csv("university_records.csv")
print(df)
