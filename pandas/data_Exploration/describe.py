import pandas as pd
"""
1= create sample data set as dictionary

"""
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}

df=pd.DataFrame(data)
print("frame data")
print(df)
print("descriptive statistics:",df.describe())