import pandas as pd
#to save and crate data 
data={
    "name":["ram","sham","akash"],
    "age":[10,20,30],
    "city":["meghaly","arunachal","up"]
}
df=pd.DataFrame(data)
print(df)
#df.to_csv("output.csv",index=False)
#df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)
print(df.info())