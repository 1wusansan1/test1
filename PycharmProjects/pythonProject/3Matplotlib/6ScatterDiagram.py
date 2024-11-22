import numpy as np
import matplotlib.pyplot as plt

'''
散点图：
    只画点，不用线连接起来。 
    可以通过每个点的坐标、颜色、大小和形状表示不同的特征值
    plt.scatter(
                x,                  # x轴坐标数组          
                y,                  # y轴坐标数组 
                marker='',          # 点型 圆圈('o')、方块('s')、三角形('^')等
                s=10,               # 大小  
                color='',           # 颜色
                edgecolor='',       # 边缘颜色
                facecolor='',       # 填充色
                zorder=''           # 图层序号
    )
'''
n = 100
# 7:  期望值  : 均值
# 8:  标准差 : 震荡幅度
# n: 数字生成数量
x1 = np.random.normal(7, 1, n)
y1 = np.random.normal(8, 1, n)

x2 = np.random.randn(n)  # 标准正态分布
y2 = np.random.rand(n)

data = np.random.normal(4, 1, (n, 1, 2))
x3 = data[:, :, 0]  # 所有面的，所有行(共1行)，第0列
y3 = data[..., 1]  # 所有面的，所有行(共1行)，第1列

plt.scatter(x1, y1, color='g', marker='d')
plt.scatter(x2, y2, color='b', marker='*')  # 标准正态分布
plt.scatter(x3, y3, color='r', marker=8)

plt.show()
