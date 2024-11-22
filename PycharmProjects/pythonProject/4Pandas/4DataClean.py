import pandas as pd
import numpy as np

'''
数据清洗:
    表中的空值一般表示形式： n/a   NA --    na 。
'''
df = pd.read_csv('property-data.csv')
print(df)
print('*' * 40)
# 把['--', 'na', 'n/a']转换成为空值代表NaN
miss_value = ['--', 'na', 'n/a']
df = pd.read_csv('property-data.csv', na_values=miss_value)
print(df)
print(df['NUM_BEDROOMS'].isnull())
'''
移除有空值的行或列:
    删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：
    DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
        how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
        thresh：设置需要多少非空值的数据才可以保留下来的。
        subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
        inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
'''
print(df)
print('======================================================移除有空值的行或列')
# inplace=False 不修改原值，生成的是新的值
df1 = df.dropna(inplace=False)
print(df1)
print('======================================================设置想要检查的行：是否有空值，有删除')
print(df)
df2 = df.dropna(subset=['ST_NUM'])
print(df2)

print('======================================================fillna()方法可以实现替换空值')

# fillna()  方法可以实现替换空值。
print(df)
df3 = df.fillna(111)
print('*' * 10)
print(df3)
print('======================================================fillna()替换指定列中的空值')
#  #替换指定列中的空值，替换为均值
print(df)
'''
Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。
'''
x = df['ST_NUM'].mean()
df4 = df['ST_NUM'].fillna(x)
print('-' * 80)
print(df4)