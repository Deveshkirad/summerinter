#4) Replace negative value with zero in numpy array using replace
import numpy as np

arr = np.array([5,-2,7,-8,10,-1])

arr[arr<0]=0

print(arr)