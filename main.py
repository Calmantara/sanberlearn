import pandas as pd
import numpy as np

data1 = {
    "id": [1, 2, 3, 4],
    "Feature1": ["a1", "a2", "a3", "a4"],
    "Feature2": ["b1", "b2", "b3", "b4"],
}

data2 = {"id": [3, 4, 5, 6, 7], "Feature3": ["c1", "c2", "c3", "c4", "c5"]}


df2 = pd.DataFrame(data2)
df = pd.DataFrame(df2)

df.insert(loc=len(df.columns), column="Baru", value="Series")
print(df)
df.iloc[1], df.iloc[2] = df.iloc[2], df.iloc[1].copy(deep = True)
print(df)
df.iloc[1], df.iloc[2] = df.iloc[2], df.iloc[1]#.copy(deep = True)
print(df)
