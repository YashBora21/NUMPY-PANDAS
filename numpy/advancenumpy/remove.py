
'''

np.delete()
'''
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new=np.delete(arr1,1)
print(new)
arr2d=np.array([[1,2,3],
                [4,5,6]])
new=np.delete(arr2d,1,0)
print(new)