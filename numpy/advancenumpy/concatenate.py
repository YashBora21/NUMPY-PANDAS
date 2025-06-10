"""
np.concatenate(arr1,arr3,axis=0)
axis =0 =vertical stacking
axis =1 =horizontl stacking

"""
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new=np.concatenate((arr1,arr2))
print(new)