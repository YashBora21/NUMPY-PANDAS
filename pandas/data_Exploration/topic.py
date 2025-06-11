"""
we nedd two imp things 
1:how big is data set
2: what are the name of the columns 
for that we use shape and column
"""


import pandas as pd
df=pd.read_json("iris.json",lines=True)

print("shape of dataset::",df.shape)
print("colums name  in dataset::",df.columns)