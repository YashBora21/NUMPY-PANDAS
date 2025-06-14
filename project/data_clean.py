import pandas as pd #use to read and process on data
import numpy as np # use for fast numerical ooperation and handling missing infinte values

#step 2 =loading the datasets 
df=pd.read_csv("data.csv")
print(f"first five row:\n{df.head()}")#to know the structure
"""print(df)"""
#checking the missing value

print(f"missing values in each collumn:\n{df.isnull().sum()}")


#now we fill the EMPLOYEE_ID,SALARY,gross,runtime  column with avg 
df["EMPLOYEE_ID"].fillna(df["EMPLOYEE_ID"].mean(),inplace=True)
df["SALARY"].fillna(df["SALARY"].mean(),inplace=True)
print(f"missing values in each collumn:\n{df.isnull().sum()}")

# Step 1: Convert to datetime, handling errors
df["HIRE_DATE"] = pd.to_datetime(df["HIRE_DATE"],format="%d-%b-%y", errors='coerce')

# Step 2: Convert datetime to int64 for interpolation (nanoseconds since epoch)
df["HIRE_DATE"] = df["HIRE_DATE"].astype("int64")

# Step 3: Interpolate the missing values
df["HIRE_DATE"] = df["HIRE_DATE"].interpolate(method="linear")

# Step 4: Convert back to datetime
df["HIRE_DATE"] = pd.to_datetime(df["HIRE_DATE"])


#replaceing infinite value conert it into  a null and the replace with mean 
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(),inplace=True)
print(f"missing values in each collumn:\n{df.isnull().sum()}")
