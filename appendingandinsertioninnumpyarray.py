import numpy as np
'''
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
newelement = np.insert(arr, 2, 50)
print(newelement)

new_element = np.append(arr, 6)

print(new_element)
'''
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7,8,9]])
                

# New column to be inserted
new_column = np.array([10, 11,12]) 

# Insert the new column at index 1 (indexing is 0-based)
arr_with_new_column1 = np.insert(arr, 0, new_column, axis=0)
arr_with_new_column2 = np.insert(arr, 1, new_column, axis=0)
arr_with_new_row1 = np.insert(arr, 0, new_column, axis=1)
arr_with_new_row2 = np.insert(arr, 1, new_column, axis=1)

#print(arr_with_new_column1)
print(arr_with_new_column2)
#print(arr_with_new_row1) 
#print(arr_with_new_row2)






