import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("作业")

plt.subplot(2, 2, 1)
x = np.arange(-10, 10, 0.1)
y = x
plt.xticks(np.arange(-10, 15, 5))  # 设置 x 轴刻度为 -10 到 10 的整数
plt.yticks(np.arange(-10, 15, 5))  # 设置 y 轴刻度为 -10 到 10 的整数
plt.plot(x, y, color='deepskyblue', label='y=x')
plt.legend(loc=2)

plt.subplot(2, 2, 2)
x2 = np.arange(-10, 10.1, 0.1)
y2 = x2 ** 2
plt.plot(x2, y2, color='red', label=r'$y=x^2$')
plt.legend(loc=0)

plt.subplot(2, 2, 3)
x3 = np.arange(-10, 10.1, 0.1)
y3 = x2 ** 3
plt.plot(x3, y3, color='forestgreen', label=r'$y=x^3$')
plt.legend(loc=2)

plt.subplot(2, 2, 4)
x4 = np.arange(0, 10.1, 0.1)
y4 = np.sqrt(x4)
plt.xticks(np.arange(0, 12.5, 2.5))
# plt.yticks(np.arange(-10, 15, 5))
plt.plot(x4, y4, color='pink', label=r'y=$\sqrt{x}$')
plt.legend(loc=2)

plt.tight_layout()
plt.show()
