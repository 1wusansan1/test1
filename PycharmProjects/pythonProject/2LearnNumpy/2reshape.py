'''
注意： array是可变的，arr2 = arr1，赋值后改变arr1的元素，arr2也会跟着变，这点和python中的list一样！！！
'''
import numpy as np

'''
重新设置维度
1. a2 = arr.reshape
2. arr.shape = (2,3)
3. a2 = np.reshape(arr, (4, 3))
'''
print('========================================a1')
a1 = np.arange(0, 12)
print(a1)
print(a1.ndim)
print(a1.shape)

print('=====================================reshape,查看官方文档api ndarray.reshape/numpy.reshape')
# 查看官网对应numpy版本的文档document
a2 = a1.reshape((1, 12))  # 1行12列
print(a2)
print(a2.shape)
a2.shape = (4, 3)  # 4行3列
print(a2)

a2 = np.reshape(a2, (12, 1))
print(a2)

a2.shape = (3, 4)

print(a2)

a2 = np.reshape(a2, (4, 3))
print(a2)
