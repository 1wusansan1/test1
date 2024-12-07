import numpy as np

print('=======================================全1的==========np.ones((5,6), dtype=np.int_)')
a1 = np.ones((5, 6), dtype=np.int_)
print(a1)

a2 = np.ones((3,))
print(a2.shape)
print('====================================全0的=============np.zeros((4,5), dtype=np.int32)')
a3 = np.zeros((3, 4,4), dtype=np.int32)

print(a3)
print('=======================元素没有初始化的========================== np.empty((3,2))')
a4 = np.empty((3, 2))
print(a4)
print('=================================具体值的================np.full((5,6), 55/arr)')
a5 = np.full((5, 6), 55)
print(a5)

a6 = np.full((5, 6), a1)
print(a6)
'''
eye 函数可以创建二维数组，对角线元素为 1.0，其他元素为 0.0。语法格式如下:
N 是行数。
M 是列数，如果省略，则生成 N x N 矩阵。
k 是对角线开始位置的索引，默认为 0，主对角线。
dtype 指定元素数据类型，默认是 float。
numpy.eye(N, M=None, k=0, dtype=float)
'''
print('===========================对角线8个1.======================np.eye(8)')
a7 = np.eye(8)
print(a7)

print('===========================转置 arr.T======================')
a1 = np.arange(0, 12)
a2 = a1.reshape((3, 4))
print(a2)
print(a2.T)

print('===========================转置 ======================')
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a3 = np.array(l1)
print(a3)

l2 = [item for item in zip(*l1)]
a4 = np.array(l2)
print(a4)

# help(np.ndarray)

# 1）使用列表推导式的方式创建一个包含1 到99的一个列表， 将列表转换为一维数组，最后将一维数组转换为3*33的二维数组。
l1 = range(1, 100)
arr = np.array(l1)
arr = arr.reshape(3,33)
print(arr)

# print(np.info(np.ndarray))
