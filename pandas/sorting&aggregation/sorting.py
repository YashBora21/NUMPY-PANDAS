"""
sorting data
we use sort value metod
df.sort_values(by="name",ascending=True,inplace=True) (true for ascending order and flase for desc)

"""
import pandas as pd
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)
"""df.sort_values(by="name",ascending=True,inplace=True)
print(df)"""
df.sort_values(by=["salary","age"],ascending=[False,True],inplace=True)
print(df)