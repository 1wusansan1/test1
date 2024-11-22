import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
4Pandas 在数据分析、数据可视化方面有着较为广泛的应用，4Pandas 对 3Matplotlib 绘图软件包的基础上单独封装了一个plot()接口，
通过调用该接口可以实现常用的绘图操作。

注：一列一个图， 行索引是X轴坐标值。元素为Y轴坐标值
'''

# 创建包含时间序列的数据
df = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range('2/1/2020',
                                                        periods=8),
             columns=list('ABCD'))
print(df)
df.plot()
plt.show()


