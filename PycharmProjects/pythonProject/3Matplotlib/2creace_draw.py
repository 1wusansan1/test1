import matplotlib.pyplot as plt
import numpy as np

# -2Π 到 2Π 范围的等差数列
x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
y = np.sin(x)
# 创建画布
fig = plt.figure(num='画布名称', figsize=(3.4, 2.8), dpi=100, facecolor='tan', edgecolor='green')
# 设置坐标轴范围
plt.xlim(-3, 3)
plt.ylim(-2, 2)
plt.plot(x, y)
plt.show()
