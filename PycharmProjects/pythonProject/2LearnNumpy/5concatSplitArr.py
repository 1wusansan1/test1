import numpy as np

'''
========================================================连接数组
'''

'''
----------------------------------------------concatenate 函数 
concatenate 函数沿指定的轴连接多个数组，他的语法格式如下：
    #a1，a2 是要连接的数组，除了连接指定轴外，其他轴大小（元素个数）相同。
    #axis 是沿指定轴的索引，默认为 0。
    numpy.concatenate((a1, a2, ...), axis=0) # axis=0沿着0轴往下拼接行/axis=1沿着1轴往右拼接列
    
拼接前：沿着哪个轴拼，拼接前会检查`剩余轴`shape是否相同，不同拼接失败。
拼接后：沿哪个轴拼接哪个轴shape就变，剩余轴的shape不变。
'''
# 沿着哪种连接，就是哪轴的shape值发生变化,其他轴值不变
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6]])

print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b.T), axis=1))


a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],[7, 8]])

print(np.concatenate((a, b), axis=1))
'''
----------------------------------------------hstack 函数
----------------------------------------------vstack: 函数  # hstack沿着0轴往下拼接行/vstack沿着1轴往右拼接列
hstack函数沿水平堆叠多个数组，相当于concatenate函数axis=1情况， 他的语法格式如下：
    numpy.hstack(tup)
vstack函数沿垂直堆叠多个数组，相当于concatenate函数axis=0情况，他的语法
    格式如下：
    numpy.vstack(tup)
'''
print('----------------------------------------------hstack: 水平方向拼接')
print(a)
print(b)
print(np.hstack((a, b.T)))
print('----------------------------------------------vstack: 垂直方向拼接')
print(np.vstack((a, b)))

'''
============================================================================分割数组
'''

'''
---------------------------------------------------------------split 函数 
split 函数沿指定轴分割多个数组，他的语法格式如下：
    ary 是要被分割的数组
    indices_or_sections 是一个整数或数组，如果是整数就用该数平均分割；如果是数组，则为沿指定轴切片操作 注意: 【左闭右开)
    axis 是轴的分割方向，默认为 0
    numpy.split(ary, indices_or_sections, axis=0)      # axis=0沿着0轴往下分割/axis=1沿着1轴往右分割列
'''
print('---------------------------------------------------split 函数 ')
a = np.arange(10, 19)
print(a)
b = np.split(a, 3)  # 平均切分成3份
print(b)
c = np.split(a, [4, 7])  # 切分起始点的下标，从4 和 7 下标开始切分
print(c)
print('------------------------------------')
a = np.arange(9).reshape(3, 3)
print(a)
b = np.split(a, 3, axis=0)
print(b)
c = np.split(a, 3, axis=1)
print(c)
print('---------------------------------------------split')
'''
hsplit 函数沿水平方向分割数组，相当于 split 函数 axis=1 情况，他的 语法格式如下：
    numpy.hsplit(ary, indices_or_sections)
vsplit 函数沿垂直方向分割数组，相当于 split 函数 axis=0 情况，他的语法格式如下：
    numpy.vsplit(ary, indices_or_sections)
'''
a = np.arange(9).reshape(3, 3)
b = np.hsplit(a, 3)
print(b)

a = np.arange(9).reshape(3, 3)
print(a)
b = np.vsplit(a, [1])
print(b)
