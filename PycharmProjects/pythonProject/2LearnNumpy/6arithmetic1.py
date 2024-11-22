import numpy as np

'''
算术运算 
    NumPy 数组对象可以使用 Python 原生的算术运算符，加、减、乘、除都可以使用。
'''
print('==========================================算术运算')
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a + b)
print(a + 10)
print(a * b)
print(a * 10)

'''
广播 
不同的形状数组或标量计算时发生广播。
'''
print('==========================================广播')
'''
标量广播
'''
print('标量广播')
a = np.array([1, 2, 3, 4])
print(a * 10)
b = np.array([[5, 6],
              [7, 8]])
print(b * 10)

'''
数组广播
广播规则：
    如果两个数组维度不相等，维度较低的数组的形状（shape）会从左侧开始填充 1，直到维度与高维数组相等。 
    如果两个数组维度相等时，要么对应轴的长度都相同，要么其中一个长度为 1，则是兼容数组可以广播。长度为 1 的轴会被扩展。
'''
print('数组广播')
a = np.array([1, 2])
b = np.array([[5, 6],
              [7, 8]])
print(a + b)  # 1. a升维 shape= (1,2)  b不变 b = (2,2) 2.此时a和b维度相同都是2维，其中a的0轴长度为1 ，会被拓展[[1, 2],[1, 2]]

'''
numpy中的函数
'''
print('==================================================================numpy中的函数')

'''
numpy中的函数
'''
print('---------------------------------------------算数运算函数')
'''
加减乘除
'''
print('--------------加减乘除')
a1 = np.array([[1, 2], [7, 8]])
a2 = np.array([[3, 6], [9, 5]])

print(a1 + a2)
print(np.add(a1, a2))

print(a1 // a2)
print(np.floor_divide(a1, a2))

print(a1 != a2)
print(np.not_equal(a1, a2))

'''
关系运算 equal,less
'''
print('---------------------------------------------关系运算')

a = np.array([1, 2])
b = np.array([[5, 6],
              [7, 8]])
print(np.equal(a, b))
print(np.less(a, b))

'''
常用随机数 ：
    # 返回一个(d0,d1,...,dn)形状的数组，元素的值介于[0.0,1.0)
    numpy.random.rand(d0, d1, ..., dn)
    #返回size形状的数组， 元素为介于[low, high)的随机整数，如果 high 省略则元素介于[0, low)随机整数
    numpy.random.randint(self, low, high=None, size=None, dtype=None)
'''
print('---------------------------------------------随机数函数')

a = np.random.rand(3, 2)
print(a)
print()
print(np.random.rand(10))
b = np.random.randint(5, 10, size=(3, 2))
print(b)

'''
正态分布随机数:
    #返回标准正态分布随机数， d0,d1...dn为shape
    numpy.random.randn(d0, d1, ..., dn)。
    #返回正态分布随机数，loc 平均值，scale 标准差, size为形状
    numpy.random.normal(loc=0.0, scale=1.0, size=None)。
'''
print('正态分布随机数')
print(np.random.randn(3, 4))
print(np.random.normal(loc=5, scale=1, size=(3, 3)))
print(np.random.normal(101, scale=5, size=(3, 3)))

'''
排序函数
'''
print('---------------------------------------------排序函数')
'''
排序函数 :
    1. 轴排序: 按照轴对数组进行排序函数 sort，他的语法格式如下：
        a 要排序的数组。
        axis 排序的轴索引，默认是-1 表示最后一个轴。
        kind 排序类型。'quicksort'（快速排序）默认值最快。另外，'mergesort'（归并排序）和'heapsort'（堆排序）
        order 排序字段
        numpy.sort(a, axis=-1, kind='quicksort', order=None)
'''
print('轴排序函数')
a = np.random.randint(0, 10, (3, 3))
print(a)
print('a sort')
print(np.sort(a))  # axis默认是-1 表示最后一个轴。
print('sort 0')
print(np.sort(a, 0))
print('sort 1')
print(np.sort(a, 1))

print('轴排序索引')
'''
轴排序索引 :
    按照轴对数组进行排序索引函数 argsort，他的语法格式如下：返回排序后的对应原数组的下标
    numpy.argsort(a, axis=-1, kind='quicksort', order=None)
'''
print(a)
print('sort -1')
print(np.argsort(a, -1))
print('sort 0')
print(np.argsort(a, 0))




