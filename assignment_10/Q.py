#Q1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] 
#Q2) Move axes of 3D array to new positions 
#Q3) Replace NaN values with average of columns 
#Q4) Replace negative value with zero in numpy array using replace

import numpy as np

#Q1
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr)
print("After replacing NaN with 0:")
print(arr)
#inter changing rown and columns
arr = arr.T
print("After interchanging rows and columns:")
print(arr)

#Q2
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Original 3D array:")
print(arr_3d)
new_arr_3d = np.transpose(arr_3d, (1, 0, 2))
print("After moving axes of 3D array:")
print(new_arr_3d)

#Q3
