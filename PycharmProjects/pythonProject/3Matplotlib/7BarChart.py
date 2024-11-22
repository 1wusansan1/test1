import matplotlib.pyplot as plt
import numpy as np

'''
柱形图：
    plt.bar(
            x,              
            y,              
            width,       #宽度   
            color='',       
            label='',       
            alpha=0.2       # 透明度
)
'''
# 设置使中文显示完整
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示完整
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示标点符号

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
x = np.arange(len(apples))
plt.xlabel('Month', fontsize=16)
plt.ylabel("Sales", fontsize=16)

plt.title("苹果/橘子销量统计图")
plt.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.bar(x - 0.2, apples, color='dodgerblue', label='苹果', width=0.4)
plt.bar(x + 0.2, oranges, color='orangered', label='橘子', width=0.4, alpha=0.1)

plt.grid(axis='y', linestyle=':')  # 追加网格线
plt.legend()
plt.show()
