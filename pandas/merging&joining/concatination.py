"""
combining data frame vericaly or horizontaly
pd.concate(df1,df2,axis=(0 row,1 cloumn),ingnore_index=true)
"""

import pandas as pd

coustomer1=pd.DataFrame({
    "id":[1,2,3,4,5,6],
    "name":["ram","sha,","kam","khan","dhan","jaan"]
})
coustomer2=pd.DataFrame({
        "id":[15,10],
        "name":["raksh","raj"]
})
concatenate_data=pd.concat([coustomer1,coustomer2],axis=0,ignore_index=True)
print(concatenate_data)