import numpy as np
arr1=np.array([1,2,np.nan,3,np.nan])
arr2=np.array([4,5,6])
#we cannot compare nan value
print(np.isnan(arr1))
#to replace
"""
np.nan_to_num(array,nan=value(defualt zero))
"""
clearedarr=np.nan_to_num(arr1,nan=1)# (arr,2)
print(clearedarr)