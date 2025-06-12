import pandas as pd
data ={
    "name":["arun","naurun","arun","naurun","karun","naurun","ja","karun","ja","ram"],
    "age":[10,20,10,40,40,40,70,20,70,70],
    "salary":[10000,2000,3000,2030,1392,1002,12392,12111,2994,2032],
    "score":[90,80,70,60,50,40,30,70,55,66]
    }
df = pd.DataFrame(data)
#grouped=df.groupby("age")["column on which peration is to be done "]
"""grouped=df.groupby("age")["salary"].sum()
print(grouped)"""

#for multiple
grouped=df.groupby(["age","name"])["salary"].sum()
print(grouped)