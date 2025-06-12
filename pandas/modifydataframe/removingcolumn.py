import pandas as pd
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)
#df.drop(clolumns=[columnname],inplace=true)inplace=ture usr to modfied real data always use it
df.drop(columns=["score"],inplace=True)
print(df)

#for multiple 
df.drop(columns=["age","salary"],inplace=True)
print(df)

