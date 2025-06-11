#ot read row data
#it have two method head and tail
#head[n]gives first nrows defualt is 5
#tail[n]display last n rows defualt is 5
import pandas as pd
df=pd.read_json("iris.json",lines=True)#Use the lines=True parameter to tell pandas to parse it as JSON Lines 

print("display first 10 rows ")
print(df.head(10))
print("display last  10 rows ")
print(df.tail())