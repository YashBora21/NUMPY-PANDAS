import numpy as np
#reshape(row,colums) only if dimensions match
num=np.array([1,2,3,4,5,6])
reshaped_arr=num.reshape(3,2)
print(reshaped_arr)
#it does not make copy it make view  