import numpy as np
'''
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

reshaped_arr = np.reshape(arr, (2, 3))
print(arr)
 
flattened_arr = arr.flatten()
print(flattened_arr)
raveled_arr = arr.ravel()
print(raveled_arr)
 '''

arr = np.array([1, 2, 3])
print(arr)
#arr_appended = np.append(arr, [4, 5])
#arr_inserted = np.insert(arr, 1, [8, 9])
arr_deleted = np.delete(arr, 1)
print(arr_deleted)