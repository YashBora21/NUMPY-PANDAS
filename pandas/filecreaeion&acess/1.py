import pandas as pd

#read data form file
#encodeing conevets text into computer 0,1
#to get data from cloud gcsfs library  need to downaload
#df= pd.read_csv("customers-100.csv",encoding="utf-8")#if not no work wiht utf-8 then use latin1 
#df=pd.read_excel("SampleXLSFile_38kb.xls")
df=pd.read_json("iris.json",lines=True)#Use the lines=True parameter to tell pandas to parse it as JSON Lines becuase contain data in lines not talble
print(df)