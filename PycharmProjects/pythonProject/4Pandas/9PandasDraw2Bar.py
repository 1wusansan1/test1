import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 柱状图

df = pd.DataFrame(np.random.rand(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# 或使用df.plot(kind="bar")
df.plot.bar()  # 纵向
plt.show()

# 横向：barh    stacked=True显示拼接数据条
df.plot.barh(stacked=True) #横向
plt.show()