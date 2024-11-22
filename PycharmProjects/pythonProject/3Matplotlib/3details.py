import numpy as np
import matplotlib.pyplot as plt

# 设置使中文显示完整
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示完整,如果坐标文本序列有中文，需要设置这个才能正常显示
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示标点符号,如果坐标文本序列有标点符号，需要设置这个才能正常显示

x = np.arange(-5, 5, 0.1)
print(x.shape)

y = x ** 2
print('--' * 20)
print(y)
print('---------------设置坐标轴名称')
# x轴y轴的名称含义
plt.xlabel('X轴')
plt.ylabel('Y轴')
print('---------------设置坐标轴刻度&范围')
# x轴刻度值序列
x_tck = np.arange(-10, 10, 2)
# x轴刻度标签文本序列 [可选]
x_txt = ['-10', '-8', '-6', '-4', '-2', '零', '2', '4', '6', '8']
# 设置x轴坐标刻度
plt.xticks(x_tck, x_txt)
# 设置坐标x轴范围
plt.xlim(-10, 10)
y_tict = np.arange(0, 25, 2)
# 设置y轴坐标刻度
plt.yticks(y_tict, y_tict.astype("U"))

# 设置坐标y轴范围
plt.ylim(0, 25)

print('-------------------------------------------------------设置坐标轴位置和颜色：left / right / bottom / top')
gcas = plt.gca()  # 拿到当前的坐标系
axis_top = gcas.spines['top']  # 获取top坐标轴
axis_top.set_color(None)  # 设置上边界坐标是颜色为无色，不显示
axis_right = gcas.spines['right']  # 获取right坐标轴
axis_right.set_color(None)  # 设置右边界坐标是颜色为无色，不显示

axis_left = gcas.spines['left']  # 获取left坐标轴
# 设置坐标轴的位置。 该方法需要传入2个元素的元组作为参数
# type:移动坐标轴的参照类型一般为data (以数据的值作为移动参照值)
axis_left.set_position(('5AataStructuresAuth', 0))
print('------------------------------------------------------------------设置坐标图例 x^2 及显示位置')
plt.plot(x, y, label=r'$x^2$')  # 图例 $开始 中间写具体的复杂公式 $结束
y1 = 2 * x
plt.plot(x, y1, label='2x')  # 图例 简单公式
# plt.legend()  # 图例显示
# 设置图例的位置
plt.legend(
    loc=0)  # 设置图例显示位置 参考官网https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend

print('=================================================================plt.title("图标题") 图标题')
plt.title("图标题")  # 图标题

'''
特殊点：
语法：
    # xarray: <序列> 所有需要标注点的水平坐标组成的序列
    # yarray: <序列> 所有需要标注点的垂直坐标组成的序列
    plt.scatter(xarray, yarray, 
                marker='',       #点型 ~ matplotlib.markers
                s='',            #大小
                edgecolor='',    #边缘色
                facecolor='',    #填充色
                zorder=3         #绘制图层编号 （编号越大，图层越靠上）
)
'''
print('================================================================================特殊点 ')
plt.scatter(x_tck,  # x坐标数组
            x_tck ** 2,  # y坐标数组
            marker="s",
            # 点形状 s:square 详见官网https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
            s=40,  # 大小
            edgecolor='pink',  # 边缘色 https://matplotlib.org/stable/gallery/color/named_colors.html
            facecolor="blue",  # 填充色 https://matplotlib.org/stable/gallery/color/named_colors.html
            zorder=3)  # 图层编号
'''
点备注:
# 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate
    plt.annotate(
                r'$frac{pi}{2}$',    #备注中显示的文本内容        
                xycoords='5AataStructuresAuth',     #备注目标点所使用的坐标系（5AataStructuresAuth)表示数据坐标系       
                xy=(x, y),           #备注目标点的坐标
                textcoords='offset points',    #备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
                xytext=(x, y),                 #备注文本的坐标位置
                fontsize=14,                   #备注文本的字体大小
                # https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch
                arrowprops=dict()           #使用字典定义文本指向目标点的箭头样式  {线样式，箭头样式}           
    )
    
    #arrowprops字典参数的常用key
    arrowprops=dict(
                    arrowstyle='',       #定义箭头样式
                    connectionstyle=''  #定义连接线的样式
    )
'''
print('================================================================================点备注')
# 设置备注
plt.annotate(
    r'$y = x ^ 2$',  # 备注中显示的文本内容
    xycoords='5AataStructuresAuth',  # 备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(4, 16),  # 备注目标点的坐标 (4,16)
    textcoords='offset points',  # 备注文本所使用的坐标系（offsetpoints表示参照点的偏移坐标系）
    xytext=(6, 18),  # 备注文本的坐标（备注的位置）
    fontsize=14,  # 备注文本的字体大小
    arrowprops=dict(arrowstyle="->", connectionstyle="angle3")  # 使用字典定义文本指向目标点的箭头样式
)

plt.show()
