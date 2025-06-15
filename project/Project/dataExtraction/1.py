import pandas as pd 
import numpy as np

df=pd.read_csv("Countries.csv")
print(df.shape)
"""print(df.isnull().sum())
print(df.describe())"""
"""print(df.columns)"""
#which country hass highest population
print(df[df["population"] == df["population"].max()]["country"])
#what is capital of country of high population
print(df[df["population"] == df["population"].max()]["capital_city"])
#for least 
print(df[df["population"] == df["population"].min()]["country"])

#top five country with democratic score
df.sort_values(by="democracy_score",ascending=False,inplace=True)
print(f"top five country with democratic score\n{df["country"].head()}")
#total region
print(df["region"].value_counts().count())
#how many contries in estern europe region

print(df["region"].value_counts()["Eastern Europe"])
#to print them
print(df[df["region"]== "Eastern Europe"]["country"])
#who is the president of second populaist country
print(df[df["population"]==df["population"].nlargest(2).iloc[1]]["political_leader"])

#how many country there leader are null
print(df[df["political_leader"].isna()]["country"].count())

#how many country has name have republic
count=0
def counting(txt):
    global count
    if "republic" in txt.lower():
        count+=1
    return txt

df["country_long"].apply(counting)
print(count)
#which country in african region have high population
df_africa=df[df["continent"] == "Africa"]
print(df_africa[df_africa["population"]==df_africa["population"].nlargest(1).iloc[0]]["country"])
