import numpy as np

'''
点积运算dot
    点积（Dot Product），作为向量间的一种基本运算，通过对应元素相乘后求和来刻画两个向量的相似度和方向关系。
    点积也称为内积或数量积 。 
    点积运算要求: 【前一个矩阵的列数和第一个矩阵的行数相等】。 !!!
    #numpy中完成点积运算的两种方式
        numpy.dot(a, b, out=None)
        ndarray.dot(b, out=None)
前一个矩阵的行分别✖后一个向量的列的乘积和：
-a1 a2 a3   -b1 b2     -a1*b1+a2*b3+a3*b5    a1*b2+a2*b4+a3*b6
-a3 a4 a5   -b3 b4   = -a3*b1+a4*b3+a5*b5    a3*b2+a4*b4+a5*b6
-a6 a7 a8   -b5 b6     -a6*b1+a7*b3+a8*b5    a6*b2+a7*b4+a8*b6
'''
print('=================================================点积运算dot')
a1 = np.random.randint(1, 5, (3, 4))
print(a1)

a2 = np.ones((4, 2))
print(a2)
print('np.dot(a1, a2):')
print(np.dot(a1, a2))  # 3,2
print('a1.dot(a2):')
print(a1.dot(a2))

'''
矩阵行列式计算
    矩阵行列式函数 numpy.linalg.det，语法如下：
        numpy.linalg.det(a)
        其实是对角线乘积差
'''
print('=================================================矩阵行列式计算np.linalg.det()')

a3 = np.random.randint(3, 8, (2, 2))
print(a3)
print('np.linalg.det(a3):')
print(np.linalg.det(a3))

'''
逆矩阵 
逆矩阵：AB=BA=E，则称 B 是 A 的逆矩阵，而 A 则被称为可逆矩阵。E 为单位矩阵(坐上到右下的写对角线为1，剩下的元素为0)。
numpy.linalg.inv(a)
'''
print('=================================================逆矩阵np.linalg.inv(arr)')
a4 = np.array([[1, 2],
               [3, 4]])
a5 = np.linalg.inv(a4)
print('np.linalg.inv(a4)逆矩阵:')
print(a5)
print('np.dot(a4, a5)单位矩阵:')
print(np.dot(a4, a5))
print(np.dot(a5, a4))


