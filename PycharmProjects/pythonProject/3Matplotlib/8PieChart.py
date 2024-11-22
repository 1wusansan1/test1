import matplotlib.pyplot as plt
import numpy as np

'''
饼状图：
    饼图（Pie Chart）是一种常用的数据可视化图形，用来展示各类别在总体中所占的比例。
    plt.pie(
            values,         # 值列表     
            spaces,         # 扇形之间的间距列表 
            labels,         # 标签列表
            colors,         # 颜色列表
            '%d%%',         # 标签所占比例格式
            shadow=True,    # 是否显示阴影
            startangle=90   # 逆时针绘制饼状图时的起始角度
            radius=1        # 半径
)
'''
plt.rcParams['font.sans-serif']=['SimHei'] #设置中文显示完整
plt.rcParams['axes.unicode_minus']=False #设置正常显示标点符号

values = [18, 13.3, 14.5, 7.3, 4.62, 51.28]
spaces = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
labels = ['Java', 'C', 'Python', 'C++', 'VB', 'Other']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold','blue']

plt.title("编程语言流行度")

plt.pie(values, spaces, labels, colors, '%d%%', shadow=True, startangle=90,radius=1)

plt.axis('equal') # 调整横轴和纵轴比例相等
plt.legend(loc=0)
plt.show()