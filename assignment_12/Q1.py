# Create numpy array and perform following operation > 
# Convert 1D array to 2D >                                                                  Done
# Print Array Attributes(Like shape, dimenssion, data type, itemsize) >                     Done
# Create a 3×3 NumPy array of all 9 >                                                       Done                        
# Create a 1D array of 10 evenly spaced values between 25 and 125 >                         Done
# Convert a Python list into a NumPy array >                                                Done
# Reverse a 1D NumPy array >                                                                Done
# Create a 4×4×3 array and extract value at its second set, first row and last column >     Done  
# Create a 4×4 and Extract Odd Rows and Even Columns >                                       
# Slice the first two rows and first two columns of econd set from a 4×4×3 array >            
# Replace all odd numbers in a NumPy array with -1 by itterating using for loop [[23, 56, 78, 93], [71, 82,13, 24]] > 
# Get the indices of non-zero elements in an array [1, 0, 2, 0, 3, 0, 4] > 
# Perform arithmetic operations on two NumPy arrays element-wise Add two NumPy arrays element by element. Multiply two NumPy arrays element by element. > 
# Write a code to compute the dot product of two NumPy arrays arr1 = [15, 20, 25] arr2 = [10,40,37]

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
r1=arr.reshape(3,3)
print(r1)

print("\nArray Attributes:")
print("Shape:",r1.shape)
print("Dimension:",r1.ndim)
print("Data Type:",r1.dtype)
print("Item Size:",r1.itemsize)

arr2=np.full((3,3),9)
print("\n3x3 Array of 9:")
print(arr2)

arr3=np.linspace(25,125,10)
print("\n1D Array of 10 evenly spaced values between 25 and 125:")
print(arr3)

python_list=[1,2,3,4,5]
numpy_array=np.array(python_list)
print("\nPython List converted to NumPy Array:")
print(numpy_array)

arr4=np.array([1,2,3,4,5])
reversed_arr4=arr4[::-1]
print("\nReversed 1D NumPy Array:")
print(reversed_arr4)

arr5=np.random.random_integers(1,10,(4,4,3))
print("\n4x4x3 Array:")
print(arr5)
print("\nValue at second set, first row and last column:")
print(arr5[1,0,-1])