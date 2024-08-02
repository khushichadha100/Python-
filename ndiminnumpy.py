# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:42:27 2024

@author: lenovo 2020
"""

import numpy as np

# Create a 1D array
arr_1d = np.array([ 1, 2, 3 ])
print("Number of dimensions for arr_1d:", arr_1d.ndim)  # Output: 1

# Create a 2D array
arr_2d = np.array([ [1, 2, 3],[4, 5, 6] ])
print(arr_2d[1][1])
print("Number of dimensions for arr_2d:", arr_2d.ndim)  # Output: 2

# Create a 3D array
arr_3d = np.array([    [ [1, 2], [3, 4] ],
                       [ [5, 6], [7, 8] ],
                       [ [9, 10],[11, 12] ] ])
print("Number of dimensions for arr_3d:", arr_3d.ndim)  # Output: 3
