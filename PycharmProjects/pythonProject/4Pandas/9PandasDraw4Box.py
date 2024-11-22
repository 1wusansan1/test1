import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 箱型图

df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
df.plot.box()
plt.show()
