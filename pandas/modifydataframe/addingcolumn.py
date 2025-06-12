import pandas as pd
data ={
    "name":["ra","ka","cha","ja","ers","jay","ram"],
    "age":[10,20,30,40,50,60,70],
    "salary":[10000,2000,3000,2030,1392,2994,2032],
    "score":[90,80,70,60,50,40,30]

}
df=pd.DataFrame(data)
#use squre breacket to add column df[colname]=data

print(df)
df["Bonus"]=df["salary"]*0.1
print(df)
#second approch using insert method 
#df.insert[pos,"column name ","data"]
df.insert(0,"ID",[11,12,13,14,15,16,17])
print(df)