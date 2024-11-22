import matplotlib.pyplot as plt
import numpy as np

'''
线型图参数缩写
'''
x = np.arange(0,10)
y1 = x ** 2
y2 = x ** 3

plt.plot(x, y1)
# plt.plot(y1)
#plt.plot(x,y1,label=r'$y=x^2$', linewidth=4, c='red')
#plt.plot(x,y1,label=r'$y=x^2$', linewidth=2, c='red', marker='^',linestyle=':')
# line: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# marker地址examples: https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
plt.plot(x,y1, 'r^:', linewidth=2, label=r'$y=x^2$') # r代表红色缩写。^代表据点的标记类型三角形，:代表点线
plt.plot(x,y2, 'go--', linewidth=4, label=r'$y=x^3$')
plt.plot()
plt.legend()
plt.show()
