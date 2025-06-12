import pandas as pd
data ={
    "name":["ra",None,None,"ja","ers","jay","ram"],
    "age":[10,20,30,40,50,None,70],
    "salary":[10000,2000,3000,2030,1392,2994,None],
    "score":[90,None,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)
print(df.isnull(),f"\nand null naues are:\n{df.isnull().sum()}")