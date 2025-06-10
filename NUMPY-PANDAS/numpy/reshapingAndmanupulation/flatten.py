"""
.ravel()-> views it affect
.flattens()->copy does not affect the orignal array
"""
import numpy as np
matrix= np.array([[2,4,6],
                  [3,4,5],
                  [2,3,4]])
print(matrix.ravel())
print(matrix.flatten())
print(matrix)