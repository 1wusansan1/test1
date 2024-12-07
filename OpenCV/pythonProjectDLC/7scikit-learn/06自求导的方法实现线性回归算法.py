import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 1、散点输入
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6],
        [0.4, 34.0], [0.8, 62.3]]
# 10*2的列表
# 转换为Numpy数组
data = np.array(data)
# 提取x和y
x_data = data[:, 0]
y_data = data[:, 1]

# 2、初始化参数
# 参数
w = 0
b = 0
# 超参数
learning_rate = 0.01


# 3、损失函数，实际代码中，反向传播没有用到，但是绘制3D图像和等高线图像用到
def loss_function(X, Y, w, b):
    _y_hat = X * w + b
    loss = np.mean(((_y_hat - Y) ** 2))
    return loss


# 创建图形对象
fig = plt.figure(figsize=(12, 6))
# 创建一个包含2行2列的布局对象
gs = gridspec.GridSpec(2, 2)

# 左上格子
ax2 = fig.add_subplot(gs[0, 0])
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

# 左下格子
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_xlabel("w")
ax3.set_ylabel("b")

# 右侧整个格子
# projection指定了这个子图是一个3D投影的图像对象
ax1 = fig.add_subplot(gs[:, 1], projection="3d")
# 构建3D的网格
w_values = np.linspace(-20, 80, 100)
b_values = np.linspace(-20, 80, 100)
W, B = np.meshgrid(w_values, b_values)
loss_values = np.zeros_like(W)

# 计算每个网格点的损失值
for i, w in enumerate(w_values):
    for j, b in enumerate(b_values):
        loss_values[j, i] = loss_function(x_data, y_data, w, b)

# ax1.plot_surface 是 Matplotlib 库中用于在三维坐标轴上绘制表面的函数 alpha=0.8修改透明度  cmap="viridis"颜色渐变
ax1.plot_surface(W, B, loss_values, alpha=0.8, cmap="viridis")

ax1.set_xlabel("w")
ax1.set_ylabel("b")
ax1.set_zlabel("loss")

# 4、开始迭代
num_iterations = 500
path = []
for n in range(1, num_iterations + 1):
    path.append((w, b))
    # 5、反向传播，更新w和b
    y_hat = w * x_data + b
    gradient_w = np.mean(2 * (y_hat - y_data) * x_data)
    gradient_b = np.mean(2 * (y_hat - y_data))
    # 更新参数
    w = w - learning_rate * gradient_w
    b = b - learning_rate * gradient_b

    # 6、显示频率设置
    if n % 10 == 0 or n == 1:
        # 7、梯度下降的显示
        ax2.cla()
        x_min = x_data.min()
        x_max = x_data.max()
        y_min = w * x_min + b
        y_max = w * x_max + b
        ax2.scatter(x_data, y_data)
        ax2.plot([x_min, x_max], [y_min, y_max], c="r")

        # contourf在 Matplotlib 库中用于绘制等高线填充图（filled contour plot）的函数。这个函数通常用于展示二维数据场的分布情况
        # levels=20等高线的圈圈改密一点
        ax3.contourf(W, B, loss_values, levels=20)
        ax3.scatter(w, b, c="r")

        ax1.scatter(w, b, loss_function(x_data, y_data, w, b), c="r")

        if len(path) > 0:
            # 把w和b分别提取出来
            path_w, path_b = zip(*path)
            # 画线
            ax3.plot(path_w, path_b, c="r")
            ax1.plot(path_w, path_b, [loss_function(x_data, y_data, np.array(path_w[i]), np.array(path_b[i])) for i in
                                      range(len(path_w))], c="r")

        plt.pause(1)
'''
ax3.contour
ax3.contour函数用于绘制非填充的等高线图。
它会根据给定的Z数据值，在X-Y平面上绘制出等高线。
可以通过levels参数来指定等高线的数量和位置。
绘制出的等高线是离散的，不会填充颜色。
ax3.contourf
ax3.contourf函数则用于绘制填充的等高线图，即根据Z数据值的不同范围，用不同的颜色填充X-Y平面上的区域。
与contour不同，contourf绘制的等高线是连续的，并且会填充颜色，使得图形更加直观和易于理解。
同样可以通过levels参数来指定填充区域的数量和位置。
contourf函数非常适合用于表示数据的连续变化和分布情况。
'''