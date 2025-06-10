import numpy as np
arr1=np.array([1,2,3,3])
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
#broatcastion expanding single   element 
result=arr1+arr2d
print(result)