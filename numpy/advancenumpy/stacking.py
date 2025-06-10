"""
combine array
verticalyy and horizontally
vstack()
hstack()
"""


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr2d=np.array([1,2,3])
print(np.vstack((arr1,arr2,arr2d)))#vertically
print(np.hstack((arr1,arr2)))#horizonatly
