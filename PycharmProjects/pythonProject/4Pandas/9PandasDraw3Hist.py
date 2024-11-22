import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 直方图

df = pd.DataFrame({'A': np.random.randn(100) + 2, 'B': np.random.randn(100), 'C': np.random.randn(100) - 2},
                  columns=['A', 'B', 'C'])
print(df)
# 指定直方柱数量为15
df.plot.hist(bins=15)
plt.show()
