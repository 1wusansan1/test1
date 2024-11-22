'''
绘制图形
matplotlib官网提供了大量例程：
以下是一些常用的 pyplot 函数：
    plot()：用于绘制折线图      !!!
    scatter()：用于绘制散点图: 示例 — 3Matplotlib 3.8.3 文档
    bar()：用于绘制垂直条形图和水平条形图
    hist()：用于绘制直方图
    pie()：用于绘制饼图
    subplot()：用于创建子图
'''
import matplotlib.pyplot as plt
import numpy as np

'''
折线图 :
    plot()函数画出一系列的点，并且用线将它们连接起来。
    x: 一维数组或列表，表示数据点在X轴上的位置
    y: 一维数组或列表，表示数据点在Y轴上的位置。
    linestyle: (可选参数) ，表示线条的样式。默认值为None默认的线条样式。实线('-')、虚线('--')、点划线('-.')、点线(':')等。
    marker: (可选参数) ，表示数据点的标记类型。默认值为None，不显示数据点的标记。 圆圈('o')、方块('s')、三角形('^')等。https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
    color: (可选参数) ，表示线条和标记的颜色。默认值为None，表示使用默认的颜色。你可以使用颜色字符串，如'red'、'blue'、'green'等，也可以使用缩写颜色
            字符串，如'r'、'b'、'g'等。
    label: (可选参数) 字符串，表示线条的标签。默认值为None。当你想为绘制的线条添加图例时，可以设置此标签。
    **kwargs: (可选参数) 这是一些可选的关键字参数，用于配置线条的其他属性，比如线条宽度、透明度等。如linewidth
    
'''

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html 折线图
x = np.arange(0, 2 * np.pi, 0.1)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin', marker='.', color='green', linewidth=1)
plt.plot(x, y2, 'ob-.', linewidth=1, label='cos')
y3 = x ** 2
plt.plot(x, y3, 'r--', label=r'$x^2$', linewidth=1)
plt.legend()
plt.show()
