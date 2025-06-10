import numpy as np
prices=np.array([100,200,300])
discount =10
final_prices=[]

#withput for loop
#broatcastion with single element 
final_prices=prices-(prices*discount/100)
print(final_prices)

#broatcastion with match dimanesion
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1+arr2)