"""
np.inset(array,index,value,axis=none)
axis=none flatten arrya
in 2d axis =0,rows insert,1=,column insert
"""
import numpy as np
arr=np.array([1,2,3,4])
new_arr=np.insert(arr,2,30)
arr2d=np.array([[1,2,3],
                [4,5,6]])
new_aarr=np.insert(arr2d,1,30,1)
print(new_aarr)
print(new_arr)