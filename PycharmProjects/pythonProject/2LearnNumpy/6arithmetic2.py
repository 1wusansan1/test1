import numpy as np

'''
=============================================================================================聚合函数: 
    可以对整个数组元素或对轴元素进行计算，获得单一值，这是聚合函数。 
    如：sum、amin、amax、mean（平均值）、average（加权平均值）、var（方差）、std（标准偏差）等
'''

'''
求和  :
    求和函数可以使用 numpy.sum 函数或数组的 numpy.ndarray.sum 方法.
    a 要求和的数组。
    axis 指定轴索引，如果 axis 没有指定是所有元素之和，如果指定轴则是该轴上的所有元素之和。
    numpy.sum(a, axis=None)
    #类似上面的函数
    numpy.ndarray.sum(axis=None)
'''
print('-----------------------------------求和')
a = np.array([[5, 6],
              [7, 8]])
a = np.random.randint(0, 9, (3, 3))
print(a)
print(np.sum(a))
print(np.sum(a, axis=-1))
print(np.sum(a, axis=0))

'''
最大值 :
    求最大值可以使用 numpy.amax 函数、numpy.nanmax 函数或数组的 ndarray.max 方法。
        numpy.amax(a, axis=None)
        #忽略 NaN（Not a Number，非数） 忽略空值
        numpy.nanmax(a, axis=None)
        #类似于amax
        numpy.ndarray.max(axis=None)
'''
print('-----------------------------------最大值')
a = np.random.randint(0, 9, (3, 3))
print(a)
print(a.max())
print(np.amax(a))

b = np.array([[5, 6], [7, np.nan]])
print(np.nanmax(b))

'''
最小值 :
    求最小值可以使用 numpy.amin 函数、numpy.nanmin 函数或数组的 ndarray.min 方法。
    numpy.amin(a, axis=None)
    #忽略 NaN
    numpy.nanmin(a, axis=None)
    numpy.ndarray.min(axis=None)
'''
print('-----------------------------------最小值')
a = np.array([[5, 6],
              [7, 8]])
print(np.amin(a))
print(np.amin(a, axis=-1))
print(np.amin(a, axis=0))
print(a.min())

'''
mean(平均值)：
   平均值 可 以使 用 numpy.mean 函 数 、 numpy.nanmean 函 数 或 数组 的 
   numpy.ndarray.mean 方法。 
   numpy.mean(a, axis=None)
   numpy.nanmean(a, axis=None)
   numpy.ndarray.mean(axis=None)
'''

print('-----------------------------------平均值')

a = np.array([[5, 6],
              [7, 8]])
print(np.mean(a))
print(np.mean(a, axis=-1))
print(np.mean(a, axis=0))
print(a.mean())

'''
 average（加权平均值） 
加权平均值可以使用 numpy.average 函数，语法如下
numpy.average(a, axis=None, weights=None)
'''
print('-----------------------------------加权平均值')

a = np.array([[5, 6],
              [7, 8]])
print(np.average(a))
print(np.average(a, axis=0))
print(np.average(a, axis=-1))
print(np.average(a, axis=0, weights=[0.3, 0.7]))

'''
unique 函数 
unique 函数可以剔除数组中重复的元素，并按照从小到大的顺序排列。语法如下：
    ar 原始数组。
    return_index 设置为 Ture，返回原始数组中的索引数组。
    axis 指定轴索。如果没有指定，多维数组会平展进行排序。
    numpy.unique(ar, return_index=False, axis=None)
'''
print('----------------------------unique 函数 ')

L = [x for x in 'Hello']
a = np.array(L)
u = np.unique(a)
print('u:')
print(u)
u, idx = np.unique(a, return_index=True)
print('idx:')
print(idx)


'''
where 函数 :
where 函数相当于三元运算符，他的语法格式如下：
    condition 是条件，如果为 True 返回 x，否则返回 y。
    x 和 y 可以是标量或数组。
    numpy.where(condition, x, y])
'''
print('----------------------------where 函数 ')
a = np.arange(5)
b = np.where(a < 3, a, a + 100)
print(b)  # array([ 0, 1, 2, 103, 104])


'''
flatten 
'''
print('----------------------------flatten 打平函数 ')

a = np.random.randint(0, 10, size=(3, 4))
print(a)
print(a.flatten())


