import numpy as np

#number dimension
arr1d=np.array([1.9,2.2,3.3])
arr2d=np.array([[1,2,3],
                [4,5,6]])
arr3d=np.array([[[1,2],[2,3],[4,5],[6,7],["fd","sas"]]])

print(arr2d.ndim)

print(arr1d.ndim)

print(arr3d.ndim)
print(arr2d.dtype)
print(arr3d.dtype)
arr=arr3d.astype(str)
print(arr)
arr1=arr1d.astype(int)
print(arr1)