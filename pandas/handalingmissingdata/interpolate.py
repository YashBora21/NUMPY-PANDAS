import pandas as pd
data ={
    "name":["ra","ram","sham","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,None,70],
    "salary":[10000,2000,3000,2030,1392,2994,None],
    "score":[90,None,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)
#methods linear time polynomial
df["age"]=df["age"].interpolate(method="linear")
print(df)