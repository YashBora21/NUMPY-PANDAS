import numpy as np
arr1=np.array([1,2,-np.inf,3,np.inf])
print(np.isinf(arr1))
clearedarr=np.nan_to_num(arr1,posinf=1000,neginf=-1000)# (arr,nan=1)
print(clearedarr)