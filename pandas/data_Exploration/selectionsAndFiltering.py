"""
1= selectiong specific column foe data manulpulation
2=filtering(conditions) rows
3=combile multiple conditions (filters)
1=squre brakects
2-boolean conditon
sleecting column
1=series
2=dataframe
column=df["column name"] for one column
subset=df[["col1","col2","col3"]]


filtering 
boolean indexing
on single conditon 
filteredrow=df[df["salary"]>50000]
for more than one condition
fitered_row=df[(df["salary]>50000)& (df["col2"]<800000)]
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

#select column
print(f"names as single return seires \n{df["name"]}")
print(f"names as multiple return data frames \n{df[["name","salary","age"]]}")
print(f"single conditon :\n{df[df["salary"]>5000]}")
print(f"multpiple conditon :\n{df[(df["salary"]>1000)& (df["age"]>20)]}")
#using or
print(f"multpiple conditon :\n{df[(df["salary"]>1000) | (df["age"]>20)]}")