import pandas as pd

"""
info()
1-no of row and collumn 
2-column names
3-data type
4- non null counts
5- memory usage of the data object
"""

import pandas as pd
df=pd.read_json("iris.json",lines=True)
print("displayint the info fo data set :",df.info())