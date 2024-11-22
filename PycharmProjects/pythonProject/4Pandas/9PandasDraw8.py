import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# 饼状图
df = pd.DataFrame(3 * np.random.rand(4), index=['go', 'java', 'c++', 'c'], columns=['L'])
print(df)
df.plot.pie(subplots=True)
plt.show()
