 
import numpy as np
'''
# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
                   
print(arr_2d)

# Append a new row
new_column = np.array([10,11,12]) 
arr_2d_with_new_row = np.append(arr_2d, [new_column], axis=0)
 
print("Array with new row:")
print(arr_2d_with_new_row)
 
''' 
import numpy as np

# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)

# Append a new column
new_column = np.array([10, 11]).reshape(-1, 1)
arr_2d_with_new_column = np.append(arr_2d, new_column, axis=1)

print("Array with new column:")
print(arr_2d_with_new_column)


