import pandas as pd
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)
#.loc[]
#df.loc[rowindex,columnname]=newvalue
df.loc[0,"salary"]=120000
print(df)
#for more rows update 
df['salary']=df["salary"]+df["salary"]*0.1
print(df)