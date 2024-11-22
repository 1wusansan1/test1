import matplotlib.pyplot as plt
import numpy as np

'''
matplotlib:
在Matplotlib库中提供了两种风格的API供开发者使用 ：
    1. Pyplot编程接口（state-based） :
        当我们使用import matplotlib.pyplot as plt语句导入pyplot模块，并使用plt.plot()绘制图形的时候，默认的Figure以及Axes等对象会自动创建以支持图
            形的绘制。Pyplot一来使得对MATLAB绘图熟悉的童鞋更加容易上手，二来屏蔽了一些底层通用的绘图对象的创建细节，使用更加简洁。 
        绘制图形 
            matplotlib官网提供了大量例程： 
            以下是一些常用的 pyplot 函数：
                plot()：用于绘制折线图
                scatter()：用于绘制散点图: 示例 — 3Matplotlib 3.8.3 文档 
                bar()：用于绘制垂直条形图和水平条形图
                hist()：用于绘制直方图
                pie()：用于绘制饼图
                subplot()：用于创建子图
    2. 面向对象的编程接口（object-based）:
        在使用面向对象的编程接口时候，我们需要自己创建图对象（Figure），自己创建Axes（一个Figure可以包含一个或者多个Axes，一个Axes可以理解为一个
            子图，使用一次plot()绘图函数便会创建一个Axes），所有对象一起才能完成一次完整的绘图。  使用面向对象编程接口有利于我们对于图形绘制的完整控
            制，但是相对于Pyplot接口可能需要书写更多的代码。
'''
# ======================================= state-based
x = np.arange(-5, 5, 0.1)
y = x ** 2
print(y)
plt.plot(x, y)
plt.show()

# ======================================= object-based
# x1 = np.linspace(-1, 1, 50)
# y1 = 2 * x1 + 1
# fig = plt.figure()
# plt.plot(x, y)
# plt.show()

# #颜色取值 https://matplotlib.org/stable/gallery/color/named_colors.html
# # 创建画布
# fig = plt.figure(num='画布名称',
#                  figsize=[5, 2.3],
#                  dpi=150,
#                  facecolor='bisque',
#                  edgecolor='red',
#                  )
# x = np.linspace(-1, 1, 50)
# y = 2 * x + 1
# ax = fig.subplots()  # 创建坐标系
# ax.plot(x, y)
# plt.show()
