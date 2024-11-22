import pandas as pd
import numpy as np

'''pandas:
    我们知道，构建和处理二维、多维数组是一项繁琐的任务。
    4Pandas 为解决这一问题， 在 ndarray 数组（NumPy 中的数组）的基础上构建出了两种不同的数据结构，分别是 Series（一维数据结构）DataFrame（二维数据结构）：
    Series 是带标签的一维数组，这里的标签可以理解为索引，但这个索引并不局限于整数，它也可以是字符类型，比如 a、b、c 等；
    DataFrame 是一种表格型数据结构，它既有行标签，又有列标签。
    DataFrame 是由Series 组成的。
'''
print('----------------------------info')
df = pd.read_csv("CASchools.csv")  # 读取csv文件
# print(df.to_string())

# print(df.info)
# print('---------------1')
# print(df.loc[0:5].to_string())
# print('---------------2')
# print(df.loc[0:5]["students"])
# print('---------------3')
# print(df["students"])
# print('----------------------------')
print(type(df))  # DataFrame
print(type(df["students"]))  # Series

print('----------------------------Series')
'''
Series:
    Series 可以保存任何数据类型，比如整数、字符串、浮点数、Python 对象等，它的标签默认为整数，从 0 开始依次递增。
        位置索引：像python列表一样自然存在的位置编号， 打印时看不到
        标签索引：人为加上的位置信息，可以是字符串，也可以是数字。（包括创建Series时程序添加的），打印时看得到
1. 创建Series对象 语法：
    pd.Series( 5AataStructuresAuth, index, dtype, copy)
    5AataStructuresAuth    输入的数据，可以是列表、常量、ndarray 数组等。
    index   索引值必须是惟一的，如果没有传递索引，则默认为 np.arrange(n)。
    dtype   表示数据类型，如果没有提供，则会自动判断得出。
    copy    表示对 5AataStructuresAuth 进行拷贝，默认为 False。
'''
print('---------------------------------------------------------------------------------------1.创建Series')
print('------------------普通创建Series对象')
arr = np.array(['a', 'b', 'c', 'd'])
s1 = pd.Series(arr)
print(s1)
print('s1----5AataStructuresAuth,index')
s1 = pd.Series(arr, [1, 2, 3, 4], dtype=str)
print(s1)

#  dict创建Series对象
print('------------------dict字典创建Series对象')
#  #传递了索引时需要将索引标签与字典中的值一一对应,索引值无法找到与其对应的值时，使用 NaN（非数字）填充!!!
s2 = pd.Series({'name': 'zs', 'age': 23, 'score': 60}, index=['name', 'score', 'age', 'aihao'])
print(s2)

# 标量创建Series对象
print('------------------标量创建Series对象 ： 如果 5AataStructuresAuth 是标量值，则必须提供索引')
s3 = pd.Series(20, index=['a', 'b', 'c', 'd'])
print(s3)

'''
如何访问 Series 序列中元素呢？分为两种方式，一种是位置索引访问；另一种是标签索引访问。 
    1. 位置索引访问
        这种访问方式与 ndarray 和 list 相同，使用元素自身的下标进行访问。
        我们知道数组的索引计数从 0 开始，这表示第一个元素存储在第 0 个索引位置上，以此类推，
        就可以获得 Series 序列中的每个元素。下面看一组简单的示例：
    2. 索引标签访问
        Series 类似于固定大小的 dict，把 index 中的索引标签当做 key，而把 Series 序列中的元素值当做 value，
        然后通过 index 索引标签来访问或者修改元素值。 
'''
print('---------------------------------------------------------------------------------------2.访问Series')
# 标量创建Series对象
s4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s4)
print(s4[0])  # 位置索引
print(s4['a'])  # 标签索引
print(s4[:3])  # 切片
print('切片2')
print(s4[:-3:-1])  # 切片

print('---------------------------------------------------------------------------------------3.Series常用属性')
# Series常用属性
'''
axes   以列表的形式返回所有行索引标签。
dtype  返回对象的数据类型。
empty  返回一个bool类型，表示Series是否为空。
ndim   返回输入数据的维数。
size   返回输入数据的元素数量。
values 以 ndarray 的形式返回 Series 对象。
index  返回一个RangeIndex对象，用来描述索引的取值范围。
'''
p1 = pd.Series(np.random.randn(5))
print(p1)
print(p1.axes)
print(p1.dtype)
print(p1.empty)
print(p1.ndim)
print(p1.size)
print(p1.values)
print(p1.index)

print('---------------------------------------------------------------------------------------4.Series常用方法')
# Series常用方法
# head()&tail()查看数据
print('------------------head()&tail()查看数据')
s = pd.Series(np.random.randn(4))
print(s)
print('--------')
print(s.head(3))
print(s.tail(3))
print('------------------isnull()&nonull()检测缺失值')
s = pd.Series(np.random.randn(4))
print(s)
print('--------')
print(s.isnull())
print(s.notnull())
print(pd.notnull(s))
print('------------------astype 类型转换')
s = pd.Series(np.random.randn(3))
s1 = s.astype(str)
print(s1)

s2 = pd.Series([1, 2, 2.2, None])
print('---s2')
print(s2)
s3 = pd.Series([1, 2, 2.2])
print('---s3')
print(s3)
s4 = s3.astype('int64')  # 有空值不能进行类型转换
print('---s4')
print(s4)
