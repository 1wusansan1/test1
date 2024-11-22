import matplotlib.pyplot as plt
import numpy as np

'''
直方图 
    使用 pyplot 中的 hist() 方法来绘制直方图， 显示数值分布的密度。hist() 方法可以用于可视化数据的分布情况，例如观察数据的中心趋势、偏态和异常值等 。
    plt.hist(
            x,         # 值列表       
            bins,      # 直方柱数量          
            color,     # 颜色       
            edgecolor  # 边缘颜色      
    )


'''
data = np.random.randn(1000)

plt.hist(data, bins=100, color='g')
plt.xlabel('Value')
plt.ylabel('Frequency')
# y轴代表出现的次数
plt.show()