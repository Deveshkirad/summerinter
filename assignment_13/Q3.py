#3) Replace NaN values with average of columns 

import numpy as np 

arr= np.array([[1,2,np.nan],
               [4,np.nan,6],
               [7,8,9]])

# Column means 
col_mean = np.nanmean(arr, axis=0)

#replace NaN with xolumn mean 
inds = np.where(np.isnan(arr))
arr[inds]= np.take(col_mean,inds[1])

print(arr)