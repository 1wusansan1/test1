import pandas as pd
import numpy as np

'''
数据加载:
    pd.read_csv(filename)
    pd.read_excel(filename)
    pd.read_sql(query, connection_object)
    pd.read_json(json_string)
    pd.read_html(url)
'''

'''
csv文件:
    采用纯文本形式，通常使用逗号作为字段之间的分隔符，每行代表一个数据记录，数据记录中的字段值可以包裹在引号或双引号中，以便正确处理包含逗号
        或换行符的复杂数据。
'''
print('-------------------------------------数据加载read_csv')
df = pd.read_csv('person.csv')
print(df)
print(df.shape)
print('-------------------------------------数据加载read_csv: 指定列作为行标签')
# 加载时将ID列作为行索引
df = pd.read_csv('person.csv', index_col='ID')
print(df)
print(df.shape)
print('---Age列转类型')
# 转类型
df['Age'] = df['Age'].astype(np.float64)
print(df)

print('-------------------------------------数据加载read_csv: 加载时转换列的数据类型')
# 加载时转换列的数据类型
df = pd.read_csv('person.csv', dtype={"Age": np.float64})
print(df)

# 修改列索引
print('-------------------------------------修改列索引: 源文件中存在列索引')
print('--方式一')
# 方式一
# 源文件中存在列索引,此时再加载时设定列索引标签，原文中的索引会被当作数据
df = pd.read_csv('person.csv', names=['a', 'b', 'c', 'd', 'e'])
print(df)
# 此时删除第一行即可
df = df.drop(0)
print(df)
print('--方式二')
# 方式二
# header=0 指定索引为0行，并代替为新的一行索引
df = pd.read_csv('person.csv', names=['a', 'b', 'c', 'd', 'e'], header=0)
print(df)

print('-------------------------------------若源文件中不存在列索引')
# 直接添加就可以了
df = pd.read_csv("person.csv", names=['a', 'b', 'c', 'd', 'e'])
print(df)
print(df.shape)

print('-------------------------------------加载时 跳过指定的行')
# 不加header=0认为0行是数据行，所以属于跳过的范围，
# skiprows=2, header=0，跳过两行后，认为0行为索引标签
# names= [] ,skiprows=2, header=0 替换0行的值作为索引后，跳过两行

df = pd.read_csv("person.csv", names=['a', 'b', 'c', 'd', 'e'], skiprows=2, header=0)
print(df)


print('-------------------------------------保存 DataFrame对象到csv文件 (index=False不生成行索引)')
df = pd.read_csv("person.csv", names=['a', 'b', 'c', 'd', 'e'], header=0)
print(df)
# index=False不生成行索引
df.to_csv('person1.csv', index=False)

