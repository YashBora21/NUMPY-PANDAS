import pandas as pd
data ={
    "name":["ra",None,None,"ja","ers","jay","ram"],
    "age":[10,20,30,40,50,None,70],
    "salary":[10000,2000,3000,2030,1392,2994,None],
    "score":[90,None,70,60,50,40,30]

}
df=pd.DataFrame(data)
print(df)

'''
dropna() if data is not nesscary
df.dropna(axis=(0 for row ,1 for column ),inplace= true)

'''
'''
df.dropna(axis=0,inplace=True)
print(df)
'''
'''
replacing with calculated value or defualt
for we use fillna 
df.fillna(value,inplace=True)
'''
'''
df.fillna(0,inplace=True)
print(df)'''
#by claculate value we wil fill with mean
df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
df["score"].fillna(df["score"].mean(),inplace=True)
print(df)
