"""
np.split() to divide in equal part 
np.vsplit()vertically
np.hsplit()horizonatlly

"""
import numpy as np
arr1=np.array([1,2,3,3])
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(np.split(arr1,2))
print(np.vsplit(arr2d,2))#vsplit only works on arrays of 2 or more dimensions  
print(np.hsplit(arr2d,2))