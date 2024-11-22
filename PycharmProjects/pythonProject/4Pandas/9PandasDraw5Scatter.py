import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 散点图
df = pd.DataFrame(np.random.rand(30, 4), columns=['a', 'b', 'c', 'd'])
# DataFrame.plot.scatter(x, y, s=None, c=None, **kwargs)[source]
# c, 可以是颜色值 也可以是个数组
# cmap 用于指定颜色映射，可选颜色映射参见：
# https://matplotlib.org/3.5.3/gallery/color/colormap_reference.html
# c='a',cmap='brg' c按照'a'列的值填充，填充范围为cmap='brg'里的
df.plot.scatter(x='a', y='b', s=20, c='a', cmap='brg')

plt.show()
