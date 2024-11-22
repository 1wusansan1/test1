import matplotlib.pyplot as plt
import numpy as np
'''
axes = fig.subplots(1,2) 获取所有坐标系
ax1 = axes[0] #第一个子图的坐标系
ax2 = axes[1] #第二个子图的坐标系
'''
fig = plt.figure("Subplot Layout", facecolor='lightgray')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

axes = fig.subplots(1,2)
print(type(axes))
print(axes.shape)
print(type(axes[0]))
ax1 = axes[0] #第一个子图的坐标系
ax2 = axes[1] #第二个子图的坐标系

ax1.plot(x, y1, label='y=sin(x)')
ax1.legend()
ax2.plot(x, y2, label='y=cos(x)')
ax2.legend()

plt.tight_layout()
# plt.legend()
plt.show()