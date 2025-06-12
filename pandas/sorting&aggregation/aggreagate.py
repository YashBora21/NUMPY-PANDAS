"""
1  summary statistics
provide summary of  column 
meamn=df.[columnname,min()]
same for max min sum
"""
import pandas as pd
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}
df=pd.DataFrame(data)

print(f"the mean of data is:{df["age"].mean()}")