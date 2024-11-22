'''
pip install numpy
NumPy（Numerical Python的缩写）是Python中用于科学计算、数据分析和机器学习的底层库，
    补充了Python语言所欠缺的数值计算能力。
NumPy在各种科学和工程领域中都得到了广泛的应用，包括但不限于：
    数据分析和处理：NumPy用于处理大量的数值数据，执行数据清洗、转换、汇总等操作。信号处理：音频、图像处理领域广泛使用NumPy来处理信号和图像数据。
    机器学习：NumPy数组通常用于存储和处理机器学习算法中的输入数据和模型参数。
    模拟和建模：科学家和工程师使用NumPy来模拟现象、进行实验和构建数值模型

虽然Python原生列表在处理小规模数据时是方便的，但是当涉及大规模数据处理和复杂的数值计算时，NumPy数组的优势显而易见：
    性能：NumPy数组经过优化，可以比Python原生列表更快地进行数值运算，这对于大型数据集和复杂计算至关重要。
    内存占用：NumPy数组更紧凑地存储数据，占用更少的内存空间，有助于处理大量数据。
    便利性：NumPy提供了丰富的数组操作函数，使得编写简洁且高效的代码更加容易。
    向量化操作：NumPy鼓励使用向量化操作，避免了在Python原生列表中使用循环的低效情况。
    提供大量的数学函数库

=====数组内元素的数据类型保持一致，为了存储空间更小，更紧促的存储
'''
import numpy as np

print('===========================================一维数组')
a = np.array([1, 2, 3])  # 数组里的元素要保持类型一致 a1 = np.array([1, 2, 3, ('zhangsan', 40)]) 这种不严格
print(a)
print(type(a))
print(a.tolist())

#
#
# a1 = np.array([1, 2, 3, ('zhangsan', 40)]) 数据类型不一致
# print(type(a1))
# print(dir(a1))
# print(a1)
# print('dtype:', a1.dtype)
# # print([1,2,3])
#
print('====================array(list(str,str1))')
a2 = np.array(('a', 'b', 'c'))
print(a2)
print(a2.dtype)  # =======数据类型
print(a2.tolist())

a1 = np.array([1, 2, 3])
print(a1.dtype)

a2 = np.array([1, 2, 3.0])
print(a2.dtype)  # float类型
print('==========================可指定数组类型dtype=np.float16')
a3 = np.array([1, 2, 3], dtype=np.float16)  # 可指定数组类型
print(a3.dtype)

a4 = np.array(['你好', '中国', 'helloworldab'])
print(a4.dtype)  # <U12 (小端格式 unicode 12) 长度最长为12的字符串
print('==========================转成指定类型a3.astype(dtype=np.int32)')
a5 = a3.astype(dtype=np.int32)  # 转成指定类型
print(a5.dtype)
print(a5)

print('======================================================== 创建一维数组的其它方式')
'''
使用 array()函数是将 Python 内置的列表或元组转换为 NumPy 数组对象， 这样做效率不高。
为此 NumPy 提供了很多创建数组的函数。
'''
print('==========================================使用 arange 函数 [左闭右开)')
'''
#start 是开始值，可以省略，默认值为 0，包含开始值
#stop 是结束值，不包含结束值。(左闭右开)
#step 是步长，默认值为 1。
#dtype 是数组元素类型。
numpy.arange([start, ]stop, [step, ] dtype=None) # [左闭右开)
注意：  步长step可以为负数，可以创建递减序列。
'''
a1 = np.arange(0, 10, 1)
print(a1)
a2 = np.arange(10, dtype=np.float16)
print(a2)
print(a2.dtype)

print('==========================================等差数列linspace函数')
'''
linspace（线性等分向量）函数创建等差数列，语法格式如下： [左闭右闭]
    start 是开始值，包含开始值。
    stop 是结束值，默认包含结束值。
    num 是设置生成的元素个数。
    endpoint 是否包含结束值（stop），False 是不包含，True 是包含，默认值是 True。
    retstep 是否返回步长（或公差），False 是不返回，默认值是 False。True是返回，当为 True 是返回值是二元组（数列数组，步长）。
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
'''
a3 = np.linspace(0, 10, 3, endpoint=False, dtype=np.int32)
print(a3, a3.dtype)
a3 = np.linspace(0, 10, 4, endpoint=False, retstep=True, dtype=np.int32)
print(a3)
mystep = a3[1]
print("步长=", mystep)

print('==========================================等比数列与 logspace 函数')
'''
logspace（对数等分向量）函数创建等比数列，语法格式如下：
    start 是开始值 base ** start。
    stop 是结束值 base ** stop。
    base 是底数。
numpy.logspace(start, stop, num=50(默认), endpoint=True, base=10.0, dtype=None)
'''
# 2^[start,end] 保留3个数值
a = np.logspace(0, 3, num=3, endpoint=False, base=2, dtype=np.int64)
print(a)

# 编写 NumPy 程序以获取有关 np.add 函数的帮助信息
#  print(np.info(np.add))
# 编写 NumPy 程序创建 20个元素的等比数列数组，指数介于 2 到 5，包括 5。（底数默认是10）
x = np.logspace(2, 5, 20)
print(x)
print('==========编写一个 NumPy 程序来创建一个从 1 到 100 的所有能够被3整除的整数数组，取值[1, 100)')
# 1）编写一个 NumPy 程序来创建一个从 1 到 100 的所有能够被3整除的整数数组，取值[1, 100)
arr = np.arange(1, 100)
arr = arr[arr % 3 == 0]
print(arr)



print('===================================a3')
t1 = [[1,2,3], [4,5,6], [7,8,9]]
a3 = np.array(t1, dtype=np.int32)
print(a3)
print('a3.ndim:', a3.ndim)
print('len(a3.shape):', len(a3.shape))
print('a3.shape:', a3.shape)
print('a3.size:', a3.size)
print('a3.dtype:', a3.dtype)
print('a3.itemsize:', a3.itemsize)
# print('a3.flags:', a3.flags)


# terminal 里执行pip list 可查看下载包的版本