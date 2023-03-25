import pandas as pd

df = pd.DataFrame([1,2,3])
# print(df)

df1 = df
# df1 = pd.DataFrame([3,4,5])

df1[0][1] = 4

# print(df1)
# print(df)

df2 = df.copy()
df2[0][1] = 5
print(df)
print(df1)
print(df2)