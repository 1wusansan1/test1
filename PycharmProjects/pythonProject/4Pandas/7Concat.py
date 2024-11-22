import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df3 = pd.DataFrame([[9, 10], [11, 12]], columns=['a', 'b'])
# ignore_index=True  行索引不会按照原来的，重新生成排序号
df = pd.concat((df1, df2, df3), ignore_index=True)
print(df)
