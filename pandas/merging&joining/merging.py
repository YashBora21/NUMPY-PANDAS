"""
same as  do ya do se jyada row ko combin karna loke sql joind
pd.merge(df1,df2,on="column name ",how"type of join")
"""

import pandas as pd

coustomer=pd.DataFrame({
    "id":[1,2,3,4,5,6],
    "name":["ram","sha,","kam","khan","dhan","jaan"]
})
df_orders=pd.DataFrame({
        "id":[1,2,5,10],
        "orderamount":[100,200,300,2000]
})
merged=pd.merge(coustomer,df_orders,on="id",how="outer")
print(merged)
"""
for right : 
   id  name  orderamount
0   1   ram          100
1   2  sha,          200
2   5  dhan          300
3  10   NaN         2000
"""
"""
for left 
   id  name  orderamount
0   1   ram        100.0
1   2  sha,        200.0
2   3   kam          NaN
3   4  khan          NaN
4   5  dhan        300.0
5   6  jaan          NaN

for inner:
   id  name  orderamount
0   1   ram          100
1   2  sha,          200
2   5  dhan          300


fro outer 
   id  name  orderamount
0   1   ram        100.0
1   2  sha,        200.0
2   3   kam          NaN
3   4  khan          NaN
4   5  dhan        300.0
5   6  jaan          NaN
6  10   NaN       2000.0
"""