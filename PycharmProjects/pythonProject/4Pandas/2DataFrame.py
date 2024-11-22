import numpy as np
import pandas as pd

'''
list: [1, 2, 3]
dict: {'a': 1, 'b': 2, 'c': 3}
上面就是一种最常见的 Python 列表和字典表达方式。而下面，我们展示的就是 Numpy 和 4Pandas 的一种构建方式。 
  a_array = np.array([
      [1, 2],
      [3, 4]])
  a_df = pd.DataFrame(
      {"a": [1, 3],
       "b": [2, 4]})
  # 打印
  print("numpy array:\n", a_array)
  print("\npandas df:\n", a_df)
  # 打印结果：
  numpy array:
   [[1 2]
   [3 4]]

  pandas df:
      a  b
  0  1  2
  1  3  4
  Pandas和Numpy与Python关系：
   你会发现，我们看到的结果中，Numpy 的是没有任何数据标签信息的，你可以认为它是纯数据。
   而 4Pandas 就像字典一样，还记录着数据的外围信息， 比如列标签（Column 名）和行标签（Row index）。
   这也是我们为什么总说 Numpy 是 Python 里的列表，而 4Pandas 是 Python 里的字典。
  异构数据表：（每列的数据类型可以不同）
   DataFrame 一个表格型的数据结构，既有行标签（index），又有列标签（columns），它也被称异构数据表，
   所谓异构，指的是表格中每列的数据类型可以不同，比如可以是字符串、整型或者浮点型等。
  从 Series 的基础上演变而来：
   DataFrame 的每一列数据都可以看成一个 Series 结构，或者把每一行看成一个Series结构。
   因此 DataFrame 其实是从 Series 的基础上演变而来。在数据分析任务中 DataFrame 的应用非常广泛，因为它描述数据的更为清晰、直观。
'''

'''
语法：
    pd.DataFrame( 5AataStructuresAuth, index, columns, dtype, copy)
    5AataStructuresAuth     输入的数据，可以是 ndarray，series，list，dict，标量以及一个 DataFrame。
    index    行标签，如果没有传递 index 值，则默认行标签是 np.arange(n)，n 代表 5AataStructuresAuth 的元素个数。
    columns  列标签，如果没有传递 columns 值，则默认列标签是 np.arange(n)。
    dtype    表示每一列的数据类型。
    copy     默认为 False，表示复制数据 5AataStructuresAuth。 
'''
# 创建DataFrame对象
print('--------------------------------------------------------------------------创建DataFrame对象')
df1 = pd.DataFrame([1, 2, 3, 4, 5])
print(df1)
print('------data传数组')
data = [['zs', 12], ['ls', 34], ['ww', 6]]
df2 = pd.DataFrame(data, columns=['name', 'age'])
print(df2)

df3 = df2.astype(str)  # 转数据类型
print(df3)
print('------data传字典{key:数组1,key2:数组2}')
data = {'name': ['zs', 'ls', 'ww', 'zl'], 'age': [34, 22, 45, 78]}
df4 = pd.DataFrame(data)
print(df4)
print('------data传数组[字典{k1:v1,k2:v2},{k1:v2,k2:v3,k3,v6}]')
data = [{"a": 1, 'b': 2, 'c': 3}, {"a": 100, 'b': 200, 'c': 500, 'd': 45}]
df5 = pd.DataFrame(data, index=['A', 'B'])
print(df5)
print('------data传字典{key1:series1,key2:series2}')
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        "two": pd.Series([11, 22, 33, 44], index=['a', 'b', 'c', 'd'])}
df6 = pd.DataFrame(data)
print(df6)

'''
操作DataFrame对象 :
    列索引操作DataFrame 
    列索引操作DataFrame（columns index）来完成数据的选取、添加和删除操作。
'''
print('--------------------------------------------------------------------------操作DataFrame对象')

print('-----------------------列索引选取数据列')
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df['one'])

print('-----------------------列索引添加数据')
df['three'] = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(df)
print('-----------------------列索引添加数据：将已经存在的数据列做相加运算')
# 将已经存在的数据列做相加运算
df['four'] = df['one'] + df['three']
print(df)
print('-----------------------列索引添加数据：到指定列')
# 注意是column参数
# 数值1代表插入到columns列表的位置索引
df.insert(1, column='score', value=[91, 90, 75, 66])
print(df)

print('-----------------------列索引删除数据列del/pop')
print('--del')
# 列索引删除数据列
del df['one']
print(df)
print('--pop')
df_pop = df.pop('two')
print(df)
print('--pop删除的内容')
print(df_pop)

# 注意： loc/iloc 允许接两个参数分别是行和列，参数之间需要使用“逗号”隔开， 接收的是行/列的标签/位置索引 。!!!
print('-------------------------行索引操作DataFrame：loc/iloc')
print(df)
print('---loc[标签索引]')
print(df)
print(df.loc['a'])  # 选取第a行
print('---iloc[位置索引]')
print(df)
print(df.iloc[2])  # 选取第2行
print('---行/列的标签索引')
print(df)
print(df.loc['a', 'score'])  # 行/列的标签索引
print(df.iloc[0, 0])

print('-------------------------行索引操作DataFrame：切片操作多行选取')
print(df)
# 左闭右开
print(df[1:3])

'''
添加数据行:
    1.使用 append() 函数，可以将新的数据行添加到 DataFrame 中，该函数会在行末追加数据行。
    2.concat()
删除数据行:
    您可以使用行索引标签，从 DataFrame 中删除某一行数据。如果索引标签存在重复，那么它们将被一起删除。
'''

print('-------------------------添加数据行：append()')
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
# 在行末追加新数据行 这种合并添加方式不建议
# df = df._append(df2)
print('--df')
print(df)
print('--df2')
print(df2)
print('--concat')
df = pd.concat([df, df2])
print(df)

print('-------------------------删除数据行：df.drop(num),索引标签存在重复，那么它们将被一起删除')
# 删除数据行,索引标签存在重复，那么它们将被一起删除。
print('--df')
print(df)
print('--df2')
print(df2)
# 注意此处调用了drop()方法
df = df.drop(0)
print(df)

'''
T      行和列转置。
axes   返回一个仅以行轴标签和列轴标签为成员的列表。
dtypes 返回每列数据的数据类型。
empty  DataFrame中没有数据或者任意坐标轴的长度为0，则返回True。
ndim   返回输入数据的维数。
shape  返回一个元组，代表DataFrame的形状
size   DataFrame中的元素数量。
values 使用 numpy 数组表示 DataFrame 中的元素值。
'''
print('--------------------------------------------------------------------------DataFrame常用属性')
d = {'Name': pd.Series(['搜狐', '新浪', "百度", '360搜索', '谷歌', '新华网', 'Bing搜索']),
     'years': pd.Series([5, 6, 15, 28, 3, 19, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# 构建DataFrame
df = pd.DataFrame(d)
print(df)
print('---------------')
print(df.T)
print('---------------')
print(df.axes)
print('---------------')
print(df.dtypes)
print('---------------')
print(df.empty)
print('---------------')
print(df.ndim)
print('---------------')
print(df.shape)
print('---------------')
print(df.size)
print('---------------')
print(df.values)

#  DataFrame常用方法
print('--------------------------------------------------------------------------DataFrame常用方法')

print('--------------head()&tail()查看数据')
print(df.head(2))
print(df.tail(2))
print('--------------shift()移动行或列')
info = pd.DataFrame({'a_data': [40, 28, 39, 32, 18],
                     'b_data': [20, 37, 41, 35, 45],
                     'c_data': [22, 17, 11, 25, 15]})
print(info)
# 移动幅度为1,向下移动一行
a = info.shift(periods=1)
print(a)

# 沿1轴移动，并将缺失值和原数值替换为52
b = info.shift(periods=2, axis=1, fill_value=52)
print(b)
