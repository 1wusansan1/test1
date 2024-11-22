import matplotlib.pyplot as plt
import numpy as np

'''子图
将一个画布，划分为多个子图，绘制多个图表。
    最常见为矩阵式布局。
    API
        plt.figure('Subplot Layout', facecolor='lightgray')
        # 拆分矩阵
            # rows: 行数
            # cols: 列数
            # num:  编号
        plt.subplot(rows, cols, num)  3,3,5
        #   1 2 3
        #   4 5 6
        #   7 8 9 
        plt.subplot(3, 3, 5)    #操作3*3的矩阵中编号为5的子图    
        plt.subplot(335)        #简写         
        #后续plt.xxxx绘制操作始终在刚选中的子图中完成
'''
fig = plt.figure("Subplot Layout", facecolor='lightgray')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(1, 2, 1)
plt.plot(x, y1)  # 在第一个子图中绘制

plt.subplot(122)  # 选中第二个子图
plt.plot(x, y2)

plt.subplot(121)  # 再次选中第一个子图
ax = plt.gca()
# 第一个子图上的上和右坐标轴不显示
ax.spines['top'].set_color(None)
ax.spines['right'].set_color(None)
plt.tight_layout  ()  # 自动调节，使得两个图更加紧凑
plt.show()
