#needed of ML
import pandas as pd
from dateutil.relativedelta import relativedelta

df = pd.read_csv("anime.csv")
print(f"first five data\n{df.head()}")

#make a new column to add episode number  by seeing
# data we can see it cotain the ep no so we extract it
#by using loc
print(df.loc[1],["Title"])
"""Title    Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...   now we extract the episode
"""
#feature Extraction
def extraxt_epi(txt):
    check=False
    data=""
    for i in txt:
        if i== ')':
           
            break
        if i== '(':
            check=True
            continue # tis skip (
        if check==True:
            data+=i
    return data

df["EpisodeNo"]=df["Title"].apply(extraxt_epi)
#now covert it into numerical
df["EpisodeNo"]=df["EpisodeNo"].str.replace(" eps","")
print(f"first five data\n{df.head()}")
print(df.loc[1])
print(df.info())
# it is object now we change data type to int
df["EpisodeNo"]=df["EpisodeNo"].astype(int)  
print(df.info())



#make a new column for timestamp
#title    Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...   now we extract the time stamp
#there are 19 char
def extract_time(txt):
    check=False
    data=""
    count =0
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1,i+20):
                data+=txt[j]
            return data
"""
other way  Example: df['Title'] = "Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473..."
df["Time_Stamp"] = df["Title"].str.extract(r"\)\s*([A-Za-z0-9\s\-]{19})")

"""

df["Time_Stamp"]=df["Title"].apply(extract_time)
"""
now extract month
"""
def month_diff(row):
    try:
        # Split start and end
        start_str, end_str = row.split(" - ")

        # Convert to datetime
        start = pd.to_datetime(start_str, format="%b %Y")
        end = pd.to_datetime(end_str, format="%b %Y")

        # Calculate month difference
        delta = relativedelta(end, start)
        total_months = delta.years * 12 + delta.months
        return total_months
    except:
        return None  # In case of parsing errors

df["Months"] = df["Time_Stamp"].apply(month_diff)
print(f"first five data\n{df.head()}")
print(df.loc[1])
print(df.info())
#top score anime 
print(df["Score"].max())

#top five score anime 
print(df["Title"].head())

# high episode
print(df.loc[df["EpisodeNo"].idxmax()])